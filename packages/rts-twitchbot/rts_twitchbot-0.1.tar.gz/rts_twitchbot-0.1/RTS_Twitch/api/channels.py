import aiohttp
from ExtraDecorators import validatetyping
from ExtraUtils.RateLimit import RateLimiter
from RTS_Twitch.overwrites import overwrites
from RTS_Twitch.memory import memory
from RTS_Twitch.toolset import paginate, single
from ExtraUtils.validate_dict import validate_dict

@validatetyping
async def get_channel_information(channel_id:int,request_channel_id:list)->dict:
    if len(request_channel_id) == 0:
        print("❌  Not enouth channel_ids to search. @ads.py(get_channel_information)")
        return {}
    if len(request_channel_id) > 100:
        print("❌  Too many channel_ids to search. @ads.py(get_channel_information)")
        return {}
    broadcast_ids = ""
    for i in request_channel_id:
        broadcast_ids += f"broadcaster_id={i}&"
    broadcast_ids = broadcast_ids[:-1]
    url= f"https://api.twitch.tv/helix/channels?{broadcast_ids}"
    return await single(channel_id,url)
        
@validatetyping
async def modify_channel_information(channel_id:int, new_data:dict)->None:
    get_user = overwrites.get_user(channel_id)
    if not get_user:
        print("❌  User not found. @ads.py(modify_channel_information)")
        return {}
    fields = ["game_id","broadcaster_language","title","delay","content_classification_lables", "is_branded_content"]
    if not all(new_data.keys in fields):
        print("❌  Invalid fields. @ads.py(modify_channel_information)\nValid fields: game_id, broadcaster_language, title, delay, content_classification_lables, is_branded_content")
        return {}
    
    url= f"https://api.twitch.tv/helix/channels?broadcaster_id={channel_id}"
    headers= {
        "Authorization": f"Bearer {get_user['access_token']}",
        "Client-ID": memory.app_id,
        "Content-Type": "application/json"
    }
    async with aiohttp.ClientSession() as session:
        async with session.patch(url, headers=headers, json=new_data) as response:
            print(await response.json())
            if not response.ok:
                print(f"❌  Error in modify_channel_information. @ads.py(modify_channel_information)->{response.text}")
                return {}
            return await response.json()
        
@validatetyping
async def get_channel_editors(channel_id:int)->dict:
    url= f"https://api.twitch.tv/helix/channels/editors?broadcaster_id={channel_id}"
    return await single(channel_id,url)
        
@validatetyping
async def get_followed_channels(channel_id:int, first:int=20, after:str="")->dict:
    url= f"https://api.twitch.tv/helix/users/follows?user_id={channel_id}&first={first}"
    return await paginate(channel_id,url)

@validatetyping
async def get_channel_followers(channel_id:int, first:int=20, after:str="")->dict:
    url= f"https://api.twitch.tv/helix/users/follows?broadcaster_id={channel_id}&first={first}"
    return await paginate(channel_id,url)