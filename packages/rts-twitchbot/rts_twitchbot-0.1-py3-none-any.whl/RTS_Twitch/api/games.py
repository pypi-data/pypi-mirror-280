from ExtraDecorators import validatetyping
from RTS_Twitch.toolset import paginate, single
from ExtraUtils.validate_dict import validate_dict

@validatetyping
async def get_top_games(channel_id:int)->dict:
    url= f"https://api.twitch.tv/helix/games/top"
    return await paginate(channel_id,url)

@validatetyping
async def get_games(channel_id:int,game_idents:list)->dict:
    string = ""
    for i in game_idents:
        if isinstance(i, int):
            string += f"id={i}&"
        if isinstance(i, str):
            string += f"name={i}&"
        else:
            return {"issue_ident":"unexpected_format"}
    url= f"https://api.twitch.tv/helix/games?{string[:-1]}"
    return await single(channel_id,url)