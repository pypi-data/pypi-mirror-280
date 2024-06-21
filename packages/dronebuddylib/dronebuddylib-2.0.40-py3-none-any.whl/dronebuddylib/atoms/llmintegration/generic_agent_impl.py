import json

from dronebuddylib.atoms.llmintegration.i_llm_agent import ILLMAgent
from dronebuddylib.utils.enums import LLMAgentNames


class GenericAgentImpl(ILLMAgent):
    """
    A class to implement an object identifier agent using an LLM (Large Language Model).
    This class provides functionalities to remember objects and identify objects in images.
    """
    SYSTEM_PROMPT_OBJECT_IDENTIFICATION = """
    You are a helpful assistant.
    """

    def __init__(self, api_key: str, model_name: str, temperature: float = None, logger_location: str = None):
        """
        Initializes the ObjectIdentifierAgentImpl with the given parameters.

        Args:
            api_key (str): The API key for accessing the LLM.
            model_name (str): The name of the model to be used.
            temperature (float, optional): The temperature setting for the model's responses.
            logger_location (str, optional): The location for logging information.
        """
        super().__init__(api_key, model_name, temperature, logger_location)
        self.set_system_prompt(self.SYSTEM_PROMPT_OBJECT_IDENTIFICATION)

    def set_manual_system_prompt(self, system_prompt):
        """
        Sets the system prompt for the LLM session.

        Args:
            system_prompt (str): The system prompt to set.
        """
        self.set_system_prompt(system_prompt)

    def get_agent_name(self):
        """
        Gets the name of the LLM agent.

        Returns:
            str: The name of the LLM agent.
        """
        return LLMAgentNames.GENERIC_AGENT.name

    def get_agent_description(self):
        """
        Gets the description of the LLM agent.

        Returns:
            str: The description of the LLM agent.
        """
        return LLMAgentNames.GENERIC_AGENT.value

    def map_results_to(self, data_structure):
        """
        Maps the results to the given data structure.

        Args:
            data_structure (object): The data structure to map the results to.
        """
        self.data_structure = data_structure

    def get_result(self):
        """
        Gets the result from the LLM.

        Returns:
            object: The result from the LLM.
        """
        result = self.get_response_from_llm().content
        formatted_result = json.loads(result)
        return formatted_result
