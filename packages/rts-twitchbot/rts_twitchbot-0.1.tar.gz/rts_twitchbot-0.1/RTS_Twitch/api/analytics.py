import aiohttp
from ExtraDecorators import validatetyping
from ExtraUtils.RateLimit import RateLimiter
from RTS_Twitch.overwrites import overwrites
from RTS_Twitch.memory import memory
from RTS_Twitch.toolset import paginate, single
from ExtraUtils.validate_dict import validate_dict

@validatetyping
async def get_extension_analytics(channel_id:int, from_date:str, to_date:str, ammount:int=20)->dict:
    querry = "?"
    if from_date:
        querry += "started_at=" + from_date +"&"
    if to_date:
        querry+=f"ended_at={to_date}&"
    if ammount:
        if ammount > 100:
            ammount = 100
        querry+=f"first={ammount}&"
    querry =  querry[:-1]
    url= f"https://api.twitch.tv/helix/analytics/extensions{querry}"
    return await paginate(channel_id,url)

@validatetyping
async def get_game_analytics(channel_id:int, from_date:str, to_date:str, ammount:int=20)->dict:

    querry = "?"
    if from_date:
        querry += "started_at=" + from_date +"&"
    if to_date:
        querry+=f"ended_at={to_date}&"
    if ammount:
        if ammount > 100:
            ammount = 100
        querry+=f"first={ammount}&"
    querry =  querry[:-1]
    url= f"https://api.twitch.tv/helix/analytics/games{querry}"

    return await paginate(channel_id,url)