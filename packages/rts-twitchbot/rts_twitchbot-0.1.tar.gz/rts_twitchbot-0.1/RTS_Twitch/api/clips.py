from ExtraDecorators import validatetyping
from RTS_Twitch.toolset import paginate, single
from ExtraUtils.validate_dict import validate_dict

@validatetyping
async def create_clip(channel_id:int,has_delay:bool=False)->dict:
    url= f"https://api.twitch.tv/helix/clips?broadcaster_id={channel_id}&has_delay={has_delay}"
    return await single(channel_id,url,"POST")

@validatetyping
async def get_clips(channel_id:int)->dict:
    url= f"https://api.twitch.tv/helix/clips?broadcaster_id={channel_id}"
    return await paginate(channel_id,url)

