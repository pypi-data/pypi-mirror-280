import unittest

from dronebuddylib.atoms.llmintegration import AgentFactory
from dronebuddylib.utils.enums import LLMAgentNames


class TestLLMIntegration(unittest.TestCase):
    def test_intent_resolving(self):
        model = "gpt-4o"
        openai_ai_key = "sk-proj-WEZlGfXOAHiv81B4GKInT3BlbkFJ3tvBHHc3nmosiRq6aInt"
        agent_factory = AgentFactory(model, openai_ai_key)

        agent = agent_factory.create_agent(LLMAgentNames.INTENT_RESOLVER)
        agent.send_text_message_to_llm_queue("user", "Fly to the nearest hospital")
        result = agent.get_result()
        print(result)