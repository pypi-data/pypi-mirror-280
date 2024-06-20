import json

from dronebuddylib.atoms.llmintegration.i_llm_agent import ILLMAgent
from dronebuddylib.atoms.llmintegration.models.intent_resolver_results import IntentResolverResults, RecognizedEntities
from dronebuddylib.models.enums import DroneCommands
from dronebuddylib.utils.enums import LLMAgentNames


class IntentResolverAgentImpl(ILLMAgent):
    SYSTEM_PROMPT_IMAGE_DESCRIBER = """
    You are a helpful assistant designed to resolve intents for a system using a drone to carry out tasks.
    The actions the system is capable of is defined in the list below
    
    #list

    if the intent cannot be resolved, return NONE, 
    if the instruction has multiple intents return MULTIPLE as the intent
    return the results in the format as below
    {
    "intent": "resolved intent",
    "phrase": "input phrase",
    "recognized_enitites": [
    { "enitity_type": "type of the entity"
    "entity_value": "value of the entity"
    }],
    "intent_type" : if the the intent can be resolved directly - DIRECT, if there are some extra steps combined to resolving this instruction or if it is a combination of intents - COMPLEX,
    confidence: confidence of the intent
    """

    def create_system_drone_action_list(self) -> str:
        list_actions = [e.name for e in DroneCommands]
        action_string = ""
        for action in list_actions:
            action_string = action_string + action + "\n"

        return action_string

    def __init__(self, api_key: str, model_name: str, temperature: float = None, logger_location: str = None):
        super().__init__(api_key, model_name, temperature, logger_location)
        drone_actions = self.create_system_drone_action_list()
        modified_prompt = self.SYSTEM_PROMPT_IMAGE_DESCRIBER.replace("#list", "\'" + drone_actions + "\'")
        self.set_system_prompt(modified_prompt)

    def get_agent_name(self):
        return LLMAgentNames.IMAGE_DESCRIBER.name

    def get_agent_description(self):
        return LLMAgentNames.IMAGE_DESCRIBER.value

    def get_result(self) -> IntentResolverResults:
        """
        Gets the description result from the LLM and formats it into an ImageDescriberResults object.

        Returns:
            ImageDescriberResults: The formatted result of the image description.
        """
        result = self.get_response_from_llm().content
        formatted_result = json.loads(result)
        # set the recognized entities
        recognized_entities = []
        for entity in formatted_result['recognized_entities']:
            recognized_entities.append(RecognizedEntities(entity['entity_type'], entity['entity_value']))

        description = IntentResolverResults(formatted_result['intent'], formatted_result['phrase'],
                                            recognized_entities, formatted_result['intent_type'],
                                            formatted_result['confidence'])

        return description
