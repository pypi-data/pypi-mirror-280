import unittest
import time

import cv2
from djitellopy import Tello

from dronebuddylib import ObjectDetectionEngine
from dronebuddylib.atoms.objectdetection.mp_object_detection_impl import MPObjectDetectionImpl
import mediapipe as mp

from dronebuddylib.atoms.objectdetection.yolo_object_detection_impl import YOLOObjectDetectionImpl
from dronebuddylib.models.engine_configurations import EngineConfigurations
from dronebuddylib.models.enums import AtomicEngineConfigurations, VisionAlgorithm
from dronebuddylib.molecules.objectidentification.object_identification_pipeline import ObjectIdentificationPipeline


# read input image


class TestObjectIdentificationPipeline(unittest.TestCase):

    def init_engine(self):
        model = "gpt-4o"
        object_name = "my cup"
        object_type = "cup"
        openai_ai_key = "sk-proj-SZIdJJozszjeVn2q885WT3BlbkFJFRODHhUYQd6gqfSRQ23F"
        pipeline = ObjectIdentificationPipeline(openai_ai_key, model)
        return pipeline, object_name, object_type

    def test_object_identification_pipeline_with_single_frame(self):
        #  object to be remembered
        image = cv2.imread(r'C:\Users\Public\projects\drone-buddy-library\test\object_images\di_cup.jpeg')

        pipeline, object_name, object_type = self.init_engine()

        pipeline.get_object_in_frame_and_verify_validity_and_remember(image, object_type, object_name)

        # frame to be searched
        todo_image = cv2.imread(r'C:\Users\Public\projects\drone-buddy-library\test\object_images\img.png')

        result = pipeline.find_object_in_frame(todo_image, object_name)
        print(result)

    def test_find_with_drone(self, object_name):
        pipeline, object_name, object_type = self.init_engine()

        drone = Tello()
        try:
            drone.connect()
            print("Battery:", drone.get_battery())
            drone.streamon()
            frame_read = drone.get_frame_read()
            test_frame = frame_read.frame
            if test_frame is None or test_frame.size == 0:
                print("Failed to get initial frame.")
                return

            count = 0
            while True:

                frame = frame_read.frame
                if frame is not None and frame.size != 0:
                    frame_color_corrected = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                    # save image to disk
                    cv2.imwrite("todo" + str(count) + ".jpg", frame_color_corrected)

                    object = pipeline.find_object_in_frame(frame_color_corrected, object_name)
                    cv2.imshow("Tello", frame_color_corrected)

                    if object:
                        print("Object found", object)
                        break
                else:
                    print("Skipped a frame.")
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break
                count += 1
                # run the loop every 2 minutes

                time.sleep(120)

        except Exception as e:
            print("Error:", e)
        finally:
            drone.streamoff()
            cv2.destroyAllWindows()


if __name__ == '__main__':
    unittest.main()
