from growwapi import GrowwAPI

async def get_portfolio() :
    API_AUTH_TOKEN = "your_token"
    groww = GrowwAPI(API_AUTH_TOKEN)
    # Optional: timeout parameter (in seconds) for the API call; default is typically set by the SDK.
    print("Calling growwapi to get the holdings")
    holdings_response = groww.get_holdings_for_user(timeout=5)
    return holdings_response

async def get_quote(name) :
    API_AUTH_TOKEN = "your_token"
    groww = GrowwAPI(API_AUTH_TOKEN)
    quote_response = groww.get_quote(
        exchange= groww.EXCHANGE_NSE,
        segment= groww.SEGMENT_CASH,
        trading_symbol=name
    )
    print(quote_response)