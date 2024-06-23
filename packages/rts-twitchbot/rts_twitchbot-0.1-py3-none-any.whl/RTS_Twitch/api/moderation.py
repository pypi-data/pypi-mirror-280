from ExtraDecorators import validatetyping
from RTS_Twitch.toolset import paginate, single
from ExtraUtils.validate_dict import validate_dict

#skiped automod 

@validatetyping
async def get_bans(channel_id:int,user_id:int=0)->dict:
    if user_id == 0:
        url= f"https://api.twitch.tv/helix/moderation/banned?broadcaster_id={channel_id}"
    else:
        url= f"https://api.twitch.tv/helix/moderation/banned?broadcaster_id={channel_id}&user_id={user_id}"
    return await paginate(channel_id,url)

@validatetyping
async def ban_user(channel_id:int,user_id:int,reason:str=None)->dict:
    url= f"https://api.twitch.tv/helix/moderation/bans?broadcaster_id={channel_id}&moderator_id={channel_id}"
    return await single(channel_id,url,"POST",data={"user_id":user_id,"reason":reason})

@validatetyping
async def unban_user(channel_id:int,user_id:int)->dict:
    url= f"https://api.twitch.tv/helix/moderation/bans?broadcaster_id={channel_id}&user_id={user_id}"
    return await single(channel_id,url,"DELETE")

@validatetyping
async def timeout_user(channel_id:int,user_id:int,duration:int,reason:str=None)->dict:
    url= f"https://api.twitch.tv/helix/moderation/bans?broadcaster_id={channel_id}&moderator_id={channel_id}"
    return await single(channel_id,url,"POST",data={"user_id":user_id,"duration":duration,"reason":reason})

@validatetyping
async def get_unban_requests(channel_id:int, status:str="pending")->dict:
    if status not in ["approved","denied","pending","acknowledged","canceled"]:
        return {"error":"unexpected_input"}
    url= f"https://api.twitch.tv/helix/moderation/unban_request?broadcaster_id={channel_id}&status={status}&moderator_id={channel_id}"
    return await paginate(channel_id,url)

@validatetyping
async def resolve_unban_request(channel_id:int,request_id:str,action:str)->dict:
    if action not in ["approve","deny","cancel"]:
        return {"error":"unexpected_input"}
    url= f"https://api.twitch.tv/helix/moderation/unban_requests?broadcaster_id={channel_id}&request_id={request_id}"
    return await single(channel_id,url,"POST",data={"action":action})