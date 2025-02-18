import pandas as pd
import os
import dotenv

# Load environment variables (e.g., API keys)
dotenv.load_dotenv()

# Import the necessary components from the rakam_systems library
from rakam_systems.components.agents.agents import Agent, Action
from rakam_systems.components.agents.actions import RAGGeneration, GenericLLMResponse
from application.engine.agent_QueryClassification.prompts import PLACEHOLDER_SYS_PROMPT
from application.engine.agent_RAG.vector_store_config import vector_store
# Placeholder system prompt

# AGENT and MODEL are set globally
AGENT_RAG = None
MODEL = "gpt-4"

# Define the AgentRag class that inherits from the Agent class
class AgentRag(Agent):
    def __init__(self, model):
        super().__init__(model=model)  # Call the parent constructor to initialize the LLM
        
        # Initialize the RAGGeneration action
        sys_prompt = "You are a knowledgeable assistant."
        prompt = "User query: {query}\nRelevant information:\n{search_results}"

        # Register the RAGGeneration action in the agent's actions
        rag_action = RAGGeneration(
            agent=self,
            sys_prompt=sys_prompt,
            prompt=prompt,
            vector_stores=[vector_store]  # Assuming vector_store is defined earlier
        )

        # Add the RAGGeneration action to the agent
        self.add_action("rag_generation", rag_action)

    # Implement the abstract choose_action method
    def choose_action(self, action_name: str):
        """
        Simple implementation of choose_action that returns the action
        based on the action name.
        """
        if action_name in self.actions:
            return self.actions[action_name]
        else:
            raise ValueError(f"Action {action_name} not found.")


# Initialize the AGENT with the model and API key
AGENT_RAG = AgentRag(model=MODEL)

