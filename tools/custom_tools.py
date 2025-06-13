custom_tools = [
{
        "type" : "function",
        "function" : {
            "name" : "get_portfolio",
            "description" : "Function to fetch my stock portfolio"
        }
    },
{
        "type" : "function",
        "function" : {
            "name" : "get_quote",
            "description" : "Function to fetch the live, real time quote of an instrument",
            "parameters" : {
                "type" : "object",
                "properties" : {
                    "name" : {
                    "type" : "string",
                    "description" : "The Trading Symbol of the instrument as defined by the exchange"
                    }
                }
            }
        }
    }
]