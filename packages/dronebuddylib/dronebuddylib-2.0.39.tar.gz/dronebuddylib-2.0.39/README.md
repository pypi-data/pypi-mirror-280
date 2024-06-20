# DroneBuddyLib

## Introduction

DroneBuddyLib is a collection of state of the art vision algorithms. You can use dronebuddylib to customize and
personalize your own drone. We support multiple functionalities.

1. Voice Recognition
2. Voice Generation
3. Object Detection
4. Object Identification
5. Intent Recognition
6. Text Recognition
7. Place recognition
8. Face Recognition

The library utilizes the latest advancements in deep learning and computer vision to provide the best possible
experience. And has a architecture following OOP principles, so that all these features are easy to use in a more plug
and play manner.

## Installation

To install the library, you can use pip. Just run the following command:

```bash 
pip install dronebuddylib
```

This will install the full library with all the features.

The installation of DroneBuddy needs the following prerequisites:

1. Python 3.9 or higher
2. Compatible pip version

> **Note:**
>
> Running `pip install dronebuddylib` will only install the drone buddy library, with only the required dependencies
> which are:
> - requests
> - numpy
> - cython
> - setuptools
> - packaging
> - pyparsing

### Installation

Each and every feature and it’s required dependencies can be installed by the following code snippet

```bash
pip install 'dronebuddylib[algorithm_name]'
```

The supported algorithms are as follows:

- FACE_RECOGNITION
- INTENT_RECOGNITION_GPT
- INTENT_RECOGNITION_SNIPS
- OBJECT_DETECTION_MP
- OBJECT_DETECTION_YOLO
- TEXT_RECOGNITION
- SPEECH_RECOGNITION_MULTI
- SPEECH_RECOGNITION_VOSK
- SPEECH_RECOGNITION_GOOGLE
- SPEECH_GENERATION
- OBJECT_IDENTIFICATION
- LLM_INTEGRATION
- PLACE_RECOGNITION

This step will only install the required dependencies for the specified algorithm.

## Usage

The library follows a simple and easy to use format, which followed for all the features.

```python
engine_configs = EngineConfigurations({})
```

EngineConfigurations class includes the parameters that are required for each algorithm to execute.
Each algorithm has defined these required parameters, in the enum class `AtomicEngineConfigurations`.

you can add the parameters to the EngineConfigurations class by using the following code snippet.

```python
engine_configs.add_configuration(AtomicEngineConfigurations.SPEECH_RECOGNITION_MULTI_ALGO_ALGORITHM_NAME,
                                 SpeechRecognitionMultiAlgoAlgorithmSupportedAlgorithms.GOOGLE.name)
```

Once the `EngineConfigurations` are added, you can start initializing the algorithm.

Each algorithm comes wrapped inside a Engine, which is capable of picking the algorithm.

For example, the functionality of speech recognition supports multiple algorithms,
you can decide which algorithm you need to use and initialize the intent recognition engine by using the following code
snippet.

```python
engine = IntentRecognitionEngine(IntentRecognitionAlgorithm.CHAT_GPT, engine_configs)
```

This architecture is followed through out the library.

Every functionality will have the same methods calls, with different implementations, which will not be reflected in the
interface level.

And you can call the methods from the `engine`, without worrying about the complex implementation details.

> **Note:**
>
> if you are missing any required parameters, the library will raise an exception during runtime, which will be helpful
> in debugging the issue.

## Supported Algorithm

### Voice Recognition

Voice recognition supports multiple algorithms, which can be used by setting the algorithm name in the configuration.

1. SpeechRecognitionMultiAlgoAlgorithmSupportedAlgorithms.GOOGLE_SPEECH_RECOGNITION
2. SpeechRecognitionMultiAlgoAlgorithmSupportedAlgorithms.VOSK_SPEECH_RECOGNITION
3. SpeechRecognitionMultiAlgoAlgorithmSupportedAlgorithms.MULTI_ALGO_SPEECH_RECOGNITION

### Voice Generation

Voice generation supports multiple algorithms, which can be used by setting the algorithm name in the configuration.

1. SpeechGenerationAlgorithm.GOOGLE_TTS_OFFLINE

### Object Detection

Object detection supports multiple algorithms, which can be used by setting the algorithm name in the configuration.

1. VisionAlgorithm.YOLO
2. VisionAlgorithm.GOOGLE_VISION
3. VisionAlgorithm.MEDIA_PIPE

### Object Identification

Object identification supports multiple algorithms, which can be used by setting the algorithm name in the
configuration.

1. ObjectRecognitionAlgorithm.YOLO_TRANSFER_LEARNING

### Intent Recognition

Intent recognition supports multiple algorithms, which can be used by setting the algorithm name in the configuration.

1. IntentRecognitionAlgorithm.CHAT_GPT
2. IntentRecognitionAlgorithm.SNIPS_NLU

### Text Recognition

Text recognition supports multiple algorithms, which can be used by setting the algorithm name in the configuration.

1. TextRecognitionAlgorithm.GOOGLE_VISION

### Place Recognition

Place recognition supports multiple algorithms, which can be used by setting the algorithm name in the configuration.

1. PlaceRecognitionAlgorithm.PLACE_RECOGNITION_KNN
2. PlaceRecognitionAlgorithm.PLACE_RECOGNITION_RF

### Face Recognition

Face recognition supports multiple algorithms, which can be used by setting the algorithm name in the configuration.

1. FaceRecognitionAlgorithm.FACE_RECOGNITION_EUCLIDEAN
2. FaceRecognitionAlgorithm.FACE_RECOGNITION_KNN

### LLM Integration

LLM integration supports multiple functionalities, which can be used by setting the algorithm name in the configuration.

1. LLMAgentNames.OBJECT_IDENTIFIER
2. LLMAgentNames.IMAGE_DESCRIBER
3. LLMAgentNames.INTENT_RESOLVER
4. LLMAgentNames.IMAGE_VALIDATOR

More details regarding the implementation, usage and installation can be found on our official documentation
at [DroneBuddyLib](https://apps.ahlab.org/drone-buddy-library/index.html)

Or you can email us at malshadz@nus.edu.sg for any queries.

