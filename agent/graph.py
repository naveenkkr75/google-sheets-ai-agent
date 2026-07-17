from langchain_google_genai import ChatGoogleGenerativeAI
from langgraph.prebuilt import create_react_agent
from langgraph.checkpoint.memory import MemorySaver

from config import GEMINI_API_KEY

from agent.generic_tools import (
    append_data,
    search_data,
    update_data,
    delete_data,
)

llm = ChatGoogleGenerativeAI(
    model="gemini-3.1-flash-lite",
    google_api_key=GEMINI_API_KEY,
    temperature=0,
)

tools = [
    append_data,
    search_data,
    update_data,
    delete_data,
]

memory = MemorySaver()

agent = create_react_agent(
    model=llm,
    tools=tools,
    checkpointer=memory,
)