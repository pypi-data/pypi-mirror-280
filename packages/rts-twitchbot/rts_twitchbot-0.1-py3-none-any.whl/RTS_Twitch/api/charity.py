import aiohttp
from ExtraDecorators import validatetyping
from ExtraUtils.RateLimit import RateLimiter
from RTS_Twitch.overwrites import overwrites
from RTS_Twitch.memory import memory
from RTS_Twitch.toolset import paginate, single

@validatetyping
async def get_charity_campaign(channel_id:int)->dict:
    url= f"https://api.twitch.tv/helix/charity"
    return await single(channel_id,url)

@validatetyping
async def get_campain_donations(channel_id:int)->dict:
    url= f"https://api.twitch.tv/helix/charity/donations?broadcaster_id={channel_id}"
    return await paginate(channel_id,url)

