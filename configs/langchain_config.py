# configs/langchain_config.py
from langchain.chat_models import init_chat_model
from langchain_core.messages import HumanMessage, AIMessage
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langgraph.checkpoint.memory import MemorySaver
from langgraph.graph import START, MessagesState, StateGraph
from functools import lru_cache
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Global memory instance (shared across all requests)
memory = MemorySaver()

# Function to initialize chat model
def get_chat_model():
    """
    Initialize and return the chat model.
    Example: Google Gemini, OpenAI, etc.
    """
    model = init_chat_model("gemini-2.5-flash", model_provider="google_genai")
    return model

# Lazy initialization of LangChain app
@lru_cache  # ensures app is created only once
def get_langchain_app():
    """
    Returns the LangChain app (StateGraph) instance.
    Lazy initialization avoids blocking FastAPI startup.
    """
    model = get_chat_model()
    workflow = StateGraph(state_schema=MessagesState)

    # Function to call the model
    def call_model(state: MessagesState):
        response = model.invoke(state["messages"])
        return {"messages": response}

    # Add node and edge to workflow
    workflow.add_node("model", call_model)
    workflow.add_edge(START, "model")

    # Compile workflow with memory
    app = workflow.compile(checkpointer=memory)
    return app

# Optional: async variant
@lru_cache
async def get_langchain_app_async():
    """
    Returns async LangChain app instance.
    """
    model = get_chat_model()
    workflow = StateGraph(state_schema=MessagesState)

    async def call_model(state: MessagesState):
        response = await model.ainvoke(state["messages"])
        return {"messages": response}

    workflow.add_node("model", call_model)
    workflow.add_edge(START, "model")

    app = workflow.compile(checkpointer=memory)
    return app
