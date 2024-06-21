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

    def test_generic(self):
        model = "gpt-4o"
        openai_ai_key = "sk-proj-WEZlGfXOAHiv81B4GKInT3BlbkFJ3tvBHHc3nmosiRq6aInt"
        agent_factory = AgentFactory(model, openai_ai_key)

        agent = agent_factory.create_agent(LLMAgentNames.GENERIC_AGENT)
        agent.set_manual_system_prompt('''You are helpful and friendly conversing assistant capable of carrying out conversations to obtain information from the user.  Always be pleasant and friendly when generating questions and if we needed be funny and carry on small talk. You will be given a goal to achieve.  
Only return the the following json format to carry on the conversation
{
"dialogue": question to be asked, if the goal is complete a thank you message
"is_goal_achieved": true if goal completed false if not
}''')
        agent.send_text_message_to_llm_queue("user", '''confirm whether the object given in the description is the correct object that the user wants to remember.
description= this is a big bottle with the name decathlon written on it''')
        result = agent.get_result()
        print(result)
