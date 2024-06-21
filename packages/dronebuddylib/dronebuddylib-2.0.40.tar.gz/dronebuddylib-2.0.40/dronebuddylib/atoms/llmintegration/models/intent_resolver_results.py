# This file contains the class IntentResolverResults which is used to store the results of the intent resolver
import json


class RecognizedEntities:
    def __init__(self, entity_type: str, entity_value: str):
        self.entity_type = entity_type
        self.entity_value = entity_value

    def to_json(self):
        return {
            'entity_type': self.entity_type,
            'entity_value': self.entity_value
        }


class IntentResolverResults:
    '''This class is used to store the results of the intent resolver
    {
    intent: "resolved intent",
    phrase: "input phrase",
    recognized_enitites: [
    { enitity_type: "type of the entity"
    entity_value: "value of the entity"
    }],
    intent_type : if the intent can be resolved directly - DIRECT, if there are some extra steps combined to resolving
     this instruction or if it is a combination of intents - COMPLEX,
    confidence: confidence of the intent as a value between 0 and 1
    '''

    def __init__(self, intent: str, phrase: str, recognized_entities: list[RecognizedEntities], intent_type: str,
                 confidence: float):
        self.intent = intent
        self.phrase = phrase
        self.recognized_entities = recognized_entities
        self.intent_type = intent_type
        self.confidence = confidence

    def to_json(self):
        return {
            'intent': self.intent,
            'phrase': self.phrase,
            'recognized_entities': [entity.to_json() for entity in self.recognized_entities],
            'intent_type': self.intent_type,
            'confidence': self.confidence
        }

    def __str__(self):
        return json.dumps(self.to_json(), indent=4)
