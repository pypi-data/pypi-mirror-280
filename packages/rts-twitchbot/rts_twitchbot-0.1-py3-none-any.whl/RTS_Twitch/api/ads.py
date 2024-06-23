import aiohttp
from ExtraDecorators import validatetyping
from ExtraUtils.RateLimit import RateLimiter
from RTS_Twitch.overwrites import overwrites
from RTS_Twitch.memory import memory
from RTS_Twitch.toolset import paginate, single
from ExtraUtils.validate_dict import validate_dict

@validatetyping
async def run_ad(channel_id:int, duration:int)->dict:
    url= f"https://api.twitch.tv/helix/channels/commercial"
    headers= {"Content-Type": "application/json"}
    data = {"broadcaster_id": channel_id,"length": duration}
    return await single(channel_id,url,"POST",headers,data)

@validatetyping
async def get_ad_schedule(channel_id:int)->dict:
    url= f"https://api.twitch.tv/helix/channels/ads?broadcaster_id={channel_id}"
    return await single(channel_id,url)
        
@validatetyping
async def snooze_ad(channel_id:int)->dict:
    url= f"https://api.twitch.tv/helix/channels/ads/schedule/snooze"
    headers= {"Content-Type": "application/json"}
    data = {"broadcaster_id": channel_id,"length": 0}
    return await single(channel_id,url,methode="POST",headers_modifier=headers,data=data)
        