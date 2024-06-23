import aiohttp
from ExtraDecorators import validatetyping
from ExtraUtils.RateLimit import RateLimiter
from ExtraUtils.validate_dict import validate_dict
from RTS_Twitch.overwrites import overwrites
from RTS_Twitch.memory import memory
from RTS_Twitch.toolset import paginate, single

@validatetyping
async def create_custom_rewards(channel_id:int, point_reward:dict):
    fields = {
        "title": {"__required": "true","__type": "string","__length": "1..45"},
        "cost": {"__type": "int","__length": "1..","__required": "true"},
        "prompt": {"__type": "string","__length": "..200"},
        "is_enabled": {"__type": "bool"},
        "background_color": {"__type": "string","__length": "6..6"},
        "is_user_input_required": {"__type": "bool"},
        "is_max_per_stream_enabled": {"__type": "bool"},
        "max_per_stream": {"__type": "int","__length": "1.."},
        "is_max_per_user_per_stream_enabled": {"__type": "bool"},
        "max_per_user_per_stream": {"__type": "int","__length": "1.."},
        "is_global_cooldown_enabled": {"__type": "bool"},
        "global_cooldown_seconds": {"__type": "int","__length": "1.."},
        "should_redemptions_skip_request_queue": {"__type": "bool"}
    }
    if not validate_dict(fields, point_reward):
        return {}

    url= f"https://api.twitch.tv/helix/channel_points/custom_rewards"
    headers= {"Content-Type": "application/json"}
    return await single(channel_id,url,"POST", headers, point_reward)
        
@validatetyping
async def delete_custom_rewards(channel_id:int, reward_id:int)->None:
    url= f"https://api.twitch.tv/helix/channel_points/custom_rewards?broadcaster_id={channel_id}&id={reward_id}"
    return await single(channel_id,url,methode="DELETE")
        
@validatetyping
async def get_custom_rewards(channel_id:int, reward_ids:list)->dict:
    string = ""
    for i in reward_ids:
        if not isinstance(i, int):
            print("❌  Invalid reward_ids. @channel_points.py(get_custom_rewards)\nreward_ids must be a list of integers")
            return {}
        string += f"&id={i}"
    url= f"https://api.twitch.tv/helix/channel_points/custom_rewards?broadcaster_id={channel_id}{string}"

    return await single(channel_id,url)
        
@validatetyping
async def get_custom_rewards_redemption(channel_id:int, reward_ids:list, status:str)->dict:
    string = ""
    for i in reward_ids:
        if not isinstance(i, int):
            print("❌  Invalid reward_ids. @channel_points.py(get_custom_rewards_redemption)\nreward_ids must be a list of integers")
            return {}
        string += f"&reward_id={i}"
    url= f"https://api.twitch.tv/helix/channel_points/custom_rewards/redemptions?broadcaster_id={channel_id}{string}&status={status}"

    return await single(channel_id,url)
        
@validatetyping
async def update_custom_rewards(channel_id:int, reward_id:int, point_reward:dict)->dict:

    fields = {
        "title": {"__type": "string","__length": "1..45"},
        "cost": {"__type": "int","__length": "1.."},
        "prompt": {"__type": "string","__length": "..200"},
        "is_enabled": {"__type": "bool"},
        "background_color": {"__type": "string","__length": "6..6"},
        "is_user_input_required": {"__type": "bool"},
        "is_max_per_stream_enabled": {"__type": "bool"},
        "max_per_stream": {"__type": "int","__length": "1.."},
        "is_max_per_user_per_stream_enabled": {"__type": "bool"},
        "max_per_user_per_stream": {"__type": "int","__length": "1.."},
        "is_global_cooldown_enabled": {"__type": "bool"},
        "global_cooldown_seconds": {"__type": "int","__length": "1.."},
        "should_redemptions_skip_request_queue": {"__type": "bool"}
    }
    if not validate_dict(fields, point_reward):
        return {}
    url= f"https://api.twitch.tv/helix/channel_points/custom_rewards?broadcaster_id={channel_id}&id={reward_id}"
    headers= {
        "Content-Type": "application/json"
    }
    return await single(channel_id,url, "POST",headers, point_reward)

@validatetyping
async def update_redemtion_status(channel_id:int, reward_id:int, redemption_id:str, status:str)->dict:
    get_user = overwrites.get_user(channel_id)
    if not get_user:
        print("❌  User not found. @channel_points.py(update_redemtion_status)")
        return {}
    if not status in ["FULFILLED", "CANCELED"]:
        print("❌  Invalid status. @channel_points.py(update_redemtion_status)\nValid statuses: FULFILLED, CANCELED")
        return {}
    url= f"https://api.twitch.tv/helix/channel_points/custom_rewards/redemptions?broadcaster_id={channel_id}&reward_id={reward_id}&id={redemption_id}"
    headers= {"Content-Type": "application/json"}
    data = {"status": status}
    return await single(channel_id,url, headers_modifier=headers, data=data)