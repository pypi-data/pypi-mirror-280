from ExtraDecorators import validatetyping
from RTS_Twitch.toolset import paginate, single
from ExtraUtils.validate_dict import validate_dict

@validatetyping
async def get_goals(channel_id:int)->dict:
    url= f"https://api.twitch.tv/helix/goals?broadcaster_id={channel_id}"
    return await single(channel_id,url)

