
import asyncio
from agent import Agent

if __name__ == "__main__":
    # async def do():
    #     query = "what is my portofolio looking at?"

    #     agent = Agent()
    #     response = await agent.process(query)
    #     print(response)
    # asyncio.run(do())
    agent = Agent()
    agent.llm_call()