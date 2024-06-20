import time

import cv2
import pkg_resources
from djitellopy import Tello
from ultralytics import YOLO

from dronebuddylib.atoms.objectidentification.object_identification_gpt_impl import ObjectIdentificationGPTImpl
from dronebuddylib.models import EngineConfigurations, AtomicEngineConfigurations
from dronebuddylib.models.acknowledgement import Acknowledgement
from dronebuddylib.utils.enums import LLMAgentNames
from dronebuddylib.utils.utils import logger


class ObjectIdentificationPipeline:

    def __init__(self, open_ai_api_key: str, open_ai_model: str):
        self.open_ai_api_key = open_ai_api_key
        self.open_ai_model = open_ai_model
        self.engine_configs = EngineConfigurations({})
        self.engine_configs.add_configuration(AtomicEngineConfigurations.OBJECT_IDENTIFICATION_GPT_API_KEY,
                                              open_ai_api_key)
        self.engine_configs.add_configuration(AtomicEngineConfigurations.OBJECT_IDENTIFICATION_GPT_MODEL, open_ai_model)
        self.object_identifying_engine = ObjectIdentificationGPTImpl(self.engine_configs)
        self.object_identifier_agent = self.object_identifying_engine.get_agent(LLMAgentNames.OBJECT_IDENTIFIER)
        self.object_describer_agent = self.object_identifying_engine.get_agent(LLMAgentNames.IMAGE_DESCRIBER)
        self.image_validator_agent = self.object_identifying_engine.get_agent(LLMAgentNames.IMAGE_VALIDATOR)

    def get_class_name(self):
        return "ObjectIdentificationPipeline"

    def describe_the_retrieved_image(self, image):
        self.object_describer_agent.send_encoded_image_message_to_llm_queue("user", "DESCRIBE", image)
        return self.object_describer_agent.get_result()

    def describe_image_for_validation(self, image):
        result = self.describe_the_retrieved_image(image)
        return result

    def get_object_in_frame_and_verify_validity_and_remember(self, image, object_type, object_name) -> Acknowledgement:
        model_name = 'yolov8n'
        yolo_model = YOLO(model_name)
        logger.log_info(self.get_class_name(), "Extracting object from frame using yolov8.")
        results = yolo_model(image)
        object_names = yolo_model.names
        count = 0
        path_name = pkg_resources.resource_filename(__name__,"resources/data/remembered_objects" )
        file_name_path = (path_name + "\\" + object_name + "_" + str(count) + ".jpg")
        final_acknowledgement = Acknowledgement("successful", "Object extracted, validated and committed to memory.")
        logger.log_info(self.get_class_name(), "Detected " + str(len(results)) + " objects in the frame")
        for result in results:

            for index, cls_tensor in enumerate(result.boxes.cls):
                cls_index = int(cls_tensor.item())  # Convert the tensor to an integer

                if object_names[int(cls_index)] == object_type:
                    logger.log_success(self.get_class_name(),
                                       "Detected object : " + object_names[int(cls_tensor.item())])

                    # extract the bounding box coordinates of the object
                    bbox_tensor = result.boxes[index].xyxy.cpu().numpy().tolist()[0]
                    # Assuming it's a PyTorch tensor
                    xmin, ymin, xmax, ymax = map(int, bbox_tensor)  # Convert to integer if necessary

                    cv2.rectangle(image, (xmin, ymin), (xmax, ymax), (0, 255, 0), 2)
                    cv2.imshow("Detected Object " + object_type, image)

                    # Crop image using OpenCV (NumPy slicing)
                    cropped_image = image[ymin:ymax, xmin:xmax]

                    # Save the cropped image using OpenCV
                    # Ensure the file_name_path is correct and includes the file extension, like '.jpg' or '.png'
                    cv2.imwrite(file_name_path, cropped_image)

                    self.remember_object(cropped_image, object_type, object_name)
                    count += 1
                    break
            final_acknowledgement = Acknowledgement("failed", "Matching object not discovered in the frame")
        if results is None or len(results) == 0:
            final_acknowledgement = Acknowledgement("failed", "No objects identified in the frame.")

        cv2.destroyAllWindows()

        return final_acknowledgement

    def validate_image(self, image, object_name) -> Acknowledgement:
        logger.log_info(self.get_class_name(), "Validating image.")
        self.image_validator_agent.send_encoded_image_message_to_llm_queue("user", "VALIDATE(" + object_name + ")",
                                                                           image)
        result = self.image_validator_agent.get_result()
        return Acknowledgement("success", "Image validated successfully.", result)

    def remember_object(self, image, object_type, object_name) -> Acknowledgement:
        logger.log_info(self.get_class_name(), "Remembering object.")
        result = self.object_identifying_engine.remember_object(image, object_type, object_name)
        return Acknowledgement("success", "Object remembered successfully.", result)

    def find_object_in_frame(self, image, object_name, threshold=0.5) -> Acknowledgement:
        logger.log_info(self.get_class_name(), "Finding object in frame.")
        result = self.object_identifying_engine.identify_object(image)
        identified_objects = result.identified_objects
        for object in identified_objects:
            print(object)
            if object.confidence > threshold and object.object_name == object_name:
                logger.log_success(self.get_class_name(), object_name + " found in frame.")
                return Acknowledgement("success", "Object found in frame.", result)

        logger.log_error(self.get_class_name(), object_name + "not found in frame.")
        return Acknowledgement("failed", "Object not found in frame.", result)
