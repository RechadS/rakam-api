import pandas as pd
import os
import dotenv

# Load environment variables (e.g., API keys)
dotenv.load_dotenv()

# Import the necessary components from the rakam_systems library
from rakam_systems.components.agents.agents import Agent, Action
from rakam_systems.components.agents.actions import ClassifyQuery
from application.engine.agent_QueryClassification.prompts import PLACEHOLDER_SYS_PROMPT
from application.engine.agent_RAG.agent_config import AGENT_RAG

# Placeholder system prompt

# AGENT and MODEL are set globally
AGENT_QUERY_CLASSIFICATION = None
MODEL = "gpt-4"

    
class DatabaseAction(Action):
    def __init__(self, agent, **kwargs):
        """Dummy action initialization"""
        
        pass

    def execute(self, **kwargs):
        """Executes the dummy action"""
        # Query classification (information, add, delete, update)


        return "Dummy Action Executed"

class DocumentSearchAction(Action):
    def __init__(self, agent, **kwargs):
        """Dummy action initialization"""

        pass

    def execute(self, **kwargs):
        """Executes the dummy action"""
        return "Dummy Action Executed"



class QueryClassificationAgent(Agent):
    def __init__(self, model: str, api_key: str, trigger_queries: pd.Series, class_names: pd.Series):
        """
        Initialize the agent with the given model and API key.
        Set up all the necessary actions for the agent.
        """
        super().__init__(model)


        self.actions = {
            # You can add more actions here, such as RAGGeneration or LLM-based actions
            "database": DatabaseAction(self),
            "documentSearch": DocumentSearchAction(self)
        }

        classify_action = ClassifyQuery(
            agent=self,
            trigger_queries = trigger_queries,
            class_names = class_names,
        )

        # Add the RAGGeneration action to the agent
        self.add_action("classify_request", classify_action)

    # TODO : Define your agent « policy function » here to choose the action
    def choose_action(self, query) -> Action:
        """
        Classifies the query and selects the appropriate action.
        """
        # If query is about Product, client or Order, search in the database
        # Register the RAGGeneration action in the agent's actions

        # Execute the RAGGeneration action via the agent
        class_name, trigger_query = self.actions['classify_request'].execute(query=query)
        # return class_name
    
        if class_name == "Information":
            results = AGENT_RAG.execute_action("rag_generation", query=query, collection_names=["shop_information_pdf_text"], stream = False)
            # current_action = self.actions.get("database", None)
        # Search in the documents
        else:
            # current_action = self.actions.get("documentSearch", None)
            results = "Contact support for more information."
        # if current_action is None:
        #    raise ValueError("Action not found in actions dictionary.")

        return results

trigger_queries = pd.Series([
# Product Queries
"Can you tell me more about this product?",
"What is the color of the chair?",

# Client Queries
"What is my customer ID?",
"Delete my account permanently.",

# Order Queries
"What is the status of my order?",
"What is the estimated delivery time?",

# Other information
"Can I get a discount on bulk purchases?",
"Are your products eco-friendly?",
"What are the top-selling products this month?",
"Do you offer product customization?",
"How can I compare product features?",
"Are there any new arrivals this week?",
"Do you have product reviews available?",
"Can I return a defective product?",
"How can I update my account details?",
"Can I reset my password?",
"How can I delete my account?",
"Do you offer loyalty rewards?",
"Can I subscribe to your newsletter?",
"How can I change my email address?",
"Is my personal data secure?",
"How do I contact customer support?",
"What are the membership benefits?",
"How can I track my order?",
"Can I modify my order after placing it?",
"What is the estimated delivery time?",
"How can I cancel my order?",
"Do you offer express shipping?",
"Can I change the shipping address?",
"How do I know if my order was successful?",
"How do I reorder a previous purchase?",
"Do you ship internationally?",
"What are the delivery charges?",
"Can I schedule a delivery time?",
"Do you offer same-day delivery?",
"How do I change my delivery address?",
"What should I do if my package is damaged?",
"Can someone else receive my delivery?",
"What happens if I'm not home for delivery?",
"Which courier services do you use?",
"Is there a tracking number for my delivery?",
"What payment methods do you accept?",
"Can I pay in installments?",
"Is my online payment secure?",
"Do you accept cryptocurrency payments?",
"Can I get an invoice for my purchase?",
"Why was my payment declined?",
"Do you offer cash on delivery?",
"Are there any transaction fees?",
"How can I apply a discount code?",
"Do you have a refund policy?",
"Where is your store located?",
"Do you have a mobile app?",
"Can I speak with a manager?",
"What are your business hours?",
"Do you offer franchise opportunities?",
"Are there any upcoming sales or promotions?",
"Can I work for your company?",
"How can I provide feedback?",
"Do you have a referral program?",
"Where can I find your terms and conditions?"
])

class_names = pd.Series(["Product"] * 2 + ["Client"] * 2 + ["Order"] * 2 +  ["Information"] * 55)

# Initialize the AGENT with the model and API key
AGENT_QUERY_CLASSIFICATION = QueryClassificationAgent(model=MODEL, api_key=os.getenv("OPENAI_API_KEY"), trigger_queries=trigger_queries, class_names=class_names)

# TODO: You can later use the CustomAgent to choose and execute actions based on the user input
