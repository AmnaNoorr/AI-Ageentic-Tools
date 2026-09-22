from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate 
from langgraph.prebuilt import create_react_agent
from tools import tools_list  # Import our tools from tools.py

import warnings
warnings.filterwarnings("ignore", message="Direct use of automatic function calling")

# 1. FIX: Update the model name to gemini-3.6-flash
llm = ChatGoogleGenerativeAI(model="gemini-3.6-flash")

agent_executor = create_react_agent(llm, tools_list)
