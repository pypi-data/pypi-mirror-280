from ExtraDecorators import validatetyping
from RTS_Twitch.toolset import paginate, single
from ExtraUtils.validate_dict import validate_dict

@validatetyping
async def get_ccl(channel_id:int)->dict:
    url= f"https://api.twitch.tv/helix/content_classification_labels"
    return await paginate(channel_id,url)

