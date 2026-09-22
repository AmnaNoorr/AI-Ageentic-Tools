from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate 
import warnings
warnings.filterwarnings("ignore", message="Direct use of automatic function calling")

# 1. FIX: Update the model name to gemini-3.6-flash
llm = ChatGoogleGenerativeAI(model="gemini-3.6-flash")
 
# 2. Create the prompt template
template = PromptTemplate.from_template(
    "You are an assistant for an AI course. Explain {topic} in two sentences."
)

# 3. Format the template with your topic
prompt = template.format(topic="the difference between BFS and DFS")

# 4. Call the model and print the output
response = llm.invoke(prompt)
if isinstance(response.content, list) and len(response.content) > 0:
    print(response.content[0].get('text', ''))
else:
    print(response.content)
