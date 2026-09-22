from langchain_core.tools import tool
@tool
def calculator(expression:str)-> str:
    """evaluates a basic arithmetic expression"""
    try:
        return(str(eval(expression, {"__builtins__":{}})))
    except Exception as e:
        return f"Error: {e}"
@tool
def word_length(word: str) -> str:
    """Returns the number of letters in a word."""
    return str(len(word))

@tool
def reverse_string(text: str) -> str:
    """Reverses the letters in a given text string or word."""
    return text[::-1]

# Export all tools in a clean list
tools_list = [calculator, word_length, reverse_string]

