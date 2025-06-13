import os
import json
from openai import AsyncAzureOpenAI, AzureOpenAI
from prompts.orchestration_agent import orchestration_agent_prompt
from tools.function_registory import function_registory  # A dictionary mapping tool names to functions
from tools.custom_tools import custom_tools

class Agent:
    def __init__(self):
        self.client = AzureOpenAI(
            azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"),
            api_key=os.getenv("AZURE_OPENAI_KEY"),
            api_version=os.getenv("AZURE_OPENAI_API_VERSION")
        )
        self.model = os.getenv("AZURE_OPENAI_MODEL")
        self.convo_history = [
            {
                "role":"system",
                "content":"youre an ai assistant"
            }
        ]

    def llm_call(self):
        completion = self.client.chat.completions.create(
            model=self.model,
            messages=self.convo_history,
            tools=custom_tools,  # tool definitions must be in OpenAI format
            tool_choice='auto'
        )
        return completion.choices[0].message

    def handle_orchestrator(self, prompt, query):
        self.add_history("system", prompt)
        self.add_history("user", query)
        response = self.llm_call()
        
        if hasattr(response, "tool_calls") and response.tool_calls:
            return self.handle(response)
        else:
            return response.content

    def add_history(self, role, content):
        self.convo_history.append({
            "role": role,
            "content": content
        })

    async def handle(self, response):
        final_result = ""

        for tool_call in response.tool_calls:
            tool_name = tool_call.function.name
            function_args = json.loads(tool_call.function.arguments)

            self.convo_history.append({
                "role": "assistant",
                "content": response.content,
                "tool_calls": [tool_call]
            })

            # Call the tool manually
            if tool_name in function_registory:
                tool_func = function_registory[tool_name]
                result = tool_func(**function_args)
            else:
                result = f"Tool '{tool_name}' not found."

            self.convo_history.append({
                "role": "tool",
                "tool_call_id": tool_call.id,
                "content": str(result)
            })

            # Pass result back to LLM
            # response = await self.llm_call()
            # final_result = response.content
            return self.convo_history

        return final_result

    async def process(self, query):
        return await self.handle_orchestrator(orchestration_agent_prompt, query)
