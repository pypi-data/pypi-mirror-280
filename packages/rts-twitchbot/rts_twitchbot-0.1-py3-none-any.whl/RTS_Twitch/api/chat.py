
from ExtraDecorators import validatetyping
from RTS_Twitch.toolset import paginate, single
from ExtraUtils.validate_dict import validate_dict

@validatetyping
async def get_chatters(channel_id:int)->dict:
    url= f"https://tmi.twitch.tv/helix/chatters?broadcaster_id={channel_id}&moderator_id={channel_id}"
    return await paginate(channel_id,url)

@validatetyping
async def get_channel_emotes(channel_id:int)->dict:
    url= f"https://api.twitch.tv/helix/chat/emotes?broadcaster_id={channel_id}"
    return await paginate(channel_id,url)

@validatetyping
async def get_global_emotes()->dict:
    url= f"https://api.twitch.tv/helix/chat/emotes/global"
    return await paginate(None,url)

@validatetyping
async def get_emote_sets(channel_id:int,emote_set_ids:list)->dict:
    string = "?"
    if len(emote_set_ids) >= 25:
        return {"error": "Too many emote_set_ids. Maximum is 25","issue_code":"list_too_long"}
    for i in emote_set_ids:
        if not isinstance(i, int):
            return {"error":"Invalid emote_set_ids. @chat.py(get_emote_sets) emote_set_ids must be a list of integers","issue_code":"type_error"}
        string += f"emote_set_id={i}&"
    url= f"https://api.twitch.tv/helix/chat/emotes/set{string[:-1]}"
    return await paginate(channel_id,url)

@validatetyping
async def get_channel_badges(channel_id:int)->dict:
    url= f"https://api.twitch.tv/helix/chat/badges?broadcaster_id={channel_id}"
    return await single(channel_id,url)

@validatetyping
async def get_global_badges(channel_id:int)->dict:
    url= f"https://api.twitch.tv/helix/chat/badges/global"
    return await single(channel_id,url)

@validatetyping
async def get_chat_settings(channel_id:int)->dict:
    url= f"https://api.twitch.tv/helix/chat/settings?broadcaster_id={channel_id}&moderator_id={channel_id}"
    return await single(channel_id,url)

@validatetyping
async def get_user_emotes(channel_id:int)->dict:
    url= f"https://api.twitch.tv/helix/chat/emotes/user?user_id={channel_id}"
    return await paginate(channel_id,url)

@validatetyping
async def update_chat_settings(channel_id:int,chat_settings:dict)->dict:
    chat_settings_rules = {
        "emote_mode": {"__type":"bool"},
        "follower_mode": {"__type":"bool"},
        "follower_mode_duration": {"__type":"int","__lenth": "0..129600"},
        "non_moderator_chat_delay": {"__type":"bool"},
        "non_moderator_chat_delay_duration": {"__type":"int","__value": [2,4,6]},
        "slow_mode": {"__type":"bool"},
        "slow_mode_wait_time": {"__type":"int","__length": "3..120"},	
        "subscriber_mode": {"__type":"bool"},
        "unique_chat_mode": {"__type":"bool"},
    }
    if not validate_dict(chat_settings_rules, chat_settings):
        return {"error":"Invalid chat_settings. @chat.py(update_chat_settings)","issue_code":"invalid_dict"}

    url= f"https://api.twitch.tv/helix/chat/settings?broadcaster_id={channel_id}"
    await single(channel_id,url,"PATCH",chat_settings)

@validatetyping
async def send_announcement(channel_id:int, message:str,color:str="primary")->dict:

    if len(message) > 500:
        return {"error":"Message too long. Maximum is 500 characters","issue_code":"message_too_long"}
    url= f"https://api.twitch.tv/helix/chat/announcements?broadcaster_id={channel_id}&moderator_id={channel_id}"
    headers= {
        "Content-Type": "application/json"
    }
    if not color in ["blue","green","orange","purple","primay"]:
        color = "primary"
    data = {
        "message": message,
        "color": color
    }
    await single(channel_id,url,"POST",data,headers_modifier=headers)
        
@validatetyping
async def send_shoutout(channel_id:int, to_broadcaster_id:int)->dict:
    url= f"https://api.twitch.tv/helix/chat/shoutouts?from_broadcaster_id={channel_id}&moderator_id={channel_id}&to_broadcaster_id={to_broadcaster_id}"
    await single(channel_id,url,"POST")
        
@validatetyping
async def send_message(channel_id:int, message:str, reply_to:str=None)->dict:
    if len(message) > 500:
        return {"error":"Message too long. Maximum is 500 characters","issue_code":"message_too_long"}
    url= f"https://api.twitch.tv/helix/chat/messages"	
    headers= {"Content-Type": "application/json"}
    data = {"message": message,"sender_id": channel_id,"broadcaster_id": channel_id}
    if reply_to:
        data["reply_to"] = reply_to
    await single(channel_id,url,"POST",data,headers_modifier=headers)
        
@validatetyping
async def get_user_chat_color(channel_id:int,user_ids:list)->dict:
    string = ""
    if len(user_ids) >= 100:
        return {"error": "Too many user_ids. Maximum is 100","issue_code":"list_too_long"}
    for i in user_ids:
        if not isinstance(i, int):
            return {"error":"Invalid user_ids. @chat.py(get_user_chat_color) user_ids must be a list of integers","issue_code":"type_error"}
        string += f"&user_id={i}"
    url= f"https://api.twitch.tv/helix/chat/colors?broadcaster_id={channel_id}" + string
    return await single(channel_id,url)

@validatetyping
async def set_user_chat_color(channel_id:int,color:str):

    if not color in ["blue","blue_violet","cadet_blue","chocolate","coral","dodger_blue","firebrick","golden_rod","green","hot_pink","orange_red","red","sea_green","spring_green","yellow_green"]:
        color = "red"
    url= f"https://api.twitch.tv/helix/chat/colors?broadcaster_id={channel_id}"
    headers= {
        "Content-Type": "application/json"
    }
    data = {
        "color": color
    }
    await single(channel_id,url,"PATCH",data,headers_modifier=headers)
