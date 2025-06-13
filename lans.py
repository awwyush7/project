import os
from langgraph.graph import StateGraph, END
from langchain_openai import AzureChatOpenAI
from langchain_core.messages import HumanMessage, ToolMessage
from langchain_core.tools import tool

# ✅ Step 1: Define the tool
@tool
def multiply(x: int, y: int) -> int:
    """Multiplies two integers and returns the result."""
    return x * y

# ✅ Step 2: Configure Azure OpenAI
llm = AzureChatOpenAI(
    openai_api_key=os.environ["AZURE_OPENAI_API_KEY"],
    azure_endpoint=os.environ["AZURE_OPENAI_ENDPOINT"],
    deployment_name=os.environ["AZURE_OPENAI_DEPLOYMENT"],
    model="gpt-35-turbo",  # or "gpt-4"
    api_version="2024-03-01-preview"
).bind_tools([multiply])

# ✅ Step 3: LLM node
def call_llm(state):
    response = llm.invoke(state["messages"])
    print("🧠 LLM:", response)
    state["messages"].append(response)
    return state

# ✅ Step 4: Tool executor node
def call_tool(state):
    tool_call = state["messages"][-1].tool_calls[0]
    tool_name = tool_call["name"]
    args = tool_call["args"]
    
    result = multiply.invoke(args)
    
    state["messages"].append(
        ToolMessage(name=tool_name, content=str(result), tool_call_id=tool_call["id"])
    )
    return state

# ✅ Step 5: Build the LangGraph
graph = StateGraph(dict)
graph.add_node("llm", call_llm)
graph.add_node("tool", call_tool)

graph.set_entry_point("llm")
graph.add_conditional_edges(
    "llm",
    lambda state: bool(getattr(state["messages"][-1], "tool_calls", [])),
    {
        True: "tool",
        False: END
    }
)
graph.add_edge("tool", "llm")

# ✅ Step 6: Compile graph and run
app = graph.compile()

initial_state = {
    "messages": [HumanMessage(content="What is 12 multiplied by 9?")]
}

final_state = app.invoke(initial_state)

# ✅ Step 7: Output final response
print("\n✅ Final Answer:", final_state["messages"][-1].content)
