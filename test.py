from langchain_ollama import ChatOllama
from langchain_core.tools import tool

@tool
def multiply(x: int, y: int) -> int:
    """Multiplies two integers."""
    return x * y

llm = ChatOllama(model="mistral").bind_tools([multiply])

response = llm.invoke("Use a function to multiply 4 and 7")
print("🔍 LLM Response:\n", response)
print("📦 tool_calls:", response.additional_kwargs.get("tool_calls"))
