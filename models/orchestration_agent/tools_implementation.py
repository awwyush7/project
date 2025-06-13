# from ...prompts.groww_agent import groww_agent_prompt
# from ...prompts.knowledge_agent import knowledge_agent_prompt
# from azure.identity import ClientSecretCredential
# from ..grow_agent.tools import groww_tools

# def get_credentials() :
#     tenant_id = 
#     client_id = 
#     client_secret = 

#     return ClientSecretCredential(tenant_id, client_id, client_secret)

# def call_groww_agent(query) : 
#     prompt = groww_agent_prompt
#     client = get_credentials()
#     response = client.chat.completions.create(
#         model = chat_model,
#         messages = [
#             {
#                 "role" : "system",
#                 "content" : f"{prompt}"
#             },
#             {
#                 "role" : "user",
#                 "content" : f"{query}"
#             }
#         ],
#         tools = groww_tools,
#         tool_choice = "auto"
#     )
#     return response.choices[0].message

# def call_knowledge_agent(query) : 
#     prompt = knowledge_agent_prompt
#     client = get_credentials()
#     response = client.chat.completions.create(
#         model = chat_model,
#         messages = [
#             {
#                 "role" : "system",
#                 "content" : f"{prompt}"
#             },
#             {
#                 "role" : "user",
#                 "content" : f"{query}"
#             }
#         ]
#     )
#     return response.choices[0].message
