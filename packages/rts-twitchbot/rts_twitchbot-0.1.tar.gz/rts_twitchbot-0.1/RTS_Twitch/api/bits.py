import aiohttp
from ExtraDecorators import validatetyping
from ExtraUtils.RateLimit import RateLimiter
from RTS_Twitch.overwrites import overwrites
from RTS_Twitch.memory import memory
from RTS_Twitch.toolset import paginate, single
from ExtraUtils.validate_dict import validate_dict


@validatetyping
async def get_leaderboard(channel_id:int, period:str, count:int)->dict:
    if period not in ["day", "week", "month", "year", "all"]:
        print("❌  Invalid period. @bits.py(get_leaderboard)\nValid periods: day, week, month, year, all")
        return {}
    get_user = overwrites.get_user(channel_id)
    if not get_user:
        print("❌  User not found. @bits.py(get_leaderboard)")
        return {}
    url= f"https://api.twitch.tv/helix/bits/leaderboard"
    headers= {
        "Authorization": f"Bearer {get_user['access_token']}",
        "Client-ID": memory.app_id,
    }
    params = {
        "period": period,
        "count": count,
    }
    return await single(channel_id,url)
        
@validatetyping
async def get_cheermotes(channel_id:int)->dict:
    url= f"https://api.twitch.tv/helix/bits/cheermotes"
    return await single(channel_id,url)
        
@validatetyping
async def get_extensions_transaction(channel_id:int,extension_id:int, transaction_ids:list)->dict:
    string = ""
    for i in transaction_ids:
        if not isinstance(i, int):
            print("❌  Invalid transaction_ids. @bits.py(get_extensions)\ntransaction_ids must be a list of integers")
            return {}
        string += f"&id={i}"
    url= f"https://api.twitch.tv/helix/extensions/transactions?extension_id={extension_id}{string}"
    return await paginate(channel_id,url)

