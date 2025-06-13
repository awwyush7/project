# Tools for groww agent which handles all the grow logic

groww_tools = [
    {
        "type" : "function",
        "function" : {
            "name" : "call_groww_agent",
            "description" : "Function to call groww_agent",
            "parameters" : {
                "type" : "object",
                "properties" : {
                    "query" : {
                    "type" : "string",
                    "description" : "The query that groww_agent to respond to"
                    }
                }
            }
        }
    },
    {
        "type" : "function",
        "function" : {
            "name" : "call_knowledge_agent",
            "description" : "Function to call knowledge base.",
            "parameters" : {
                "type" : "object",
                "properties" : {
                    "query" : {
                    "type" : "string",
                    "description" : "The query that knowledge_agent needs to respond to"
                    }
                }
            }
        }
    }
]