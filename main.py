from agent import agent_executor  # Import the compiled agent from agent.py

def run_agent_query(query: str):
    print("\n" + "="*60)
    print(f"USER QUERY: {query}")
    print("="*60)
    
    # Stream the steps so you can capture the visual trace for your report
    events = agent_executor.stream(
        {"messages": [("user", query)]},
        stream_mode="values"
    )
    
    for event in events:
        if "messages" in event:
            latest_message = event["messages"][-1]
            
            # Print agent's reasoning or tool calls
            if latest_message.type == "ai":
                if latest_message.tool_calls:
                    print(f"\n[THOUGHT/ACTION] Agent decides to call tool:")
                    for tool_call in latest_message.tool_calls:
                        print(f"   -> Tool Name: {tool_call['name']}")
                        print(f"   -> Arguments: {tool_call['args']}")
                elif latest_message.content:
                    print(f"\n[FINAL ANSWER]:\n{latest_message.content}")
            
            # Print tool outputs back to the agent
            elif latest_message.type == "tool":
                print(f"\n[OBSERVATION] Tool output received:")
                print(f"   -> Result: {latest_message.content}")

# Execute the queries required by your lab assignment
if __name__ == "__main__":
    # Query 1: Multi-step tool call (WordLength -> Calculator)
    run_agent_query("What is the length of the word 'Intelligence' multiplied by 12?")
    
    # Query 2: Custom 3rd tool call + basic math (Reverse String -> Calculator)
    run_agent_query("Reverse the word 'Artificial' and calculate what 144 divided by 4 is.")
