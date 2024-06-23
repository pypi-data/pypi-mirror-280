from ExtraDecorators import validatetyping
from RTS_Twitch.toolset import paginate, single
from ExtraUtils.validate_dict import validate_dict

@validatetyping
async def get_drop_entitlements(channel_id:int)->dict:
    url= f"https://api.twitch.tv/helix/entitlements/drops"
    return await paginate(channel_id,url)

@validatetyping
async def update_drop_entitlements(channel_id:int,to_status:str,entitlement_ids:list)->dict:
    if to_status not in ["CLAIMED", "FULFILLED"]:
        print("❌  Invalid to_status. @entitlements.py(update_drop_entitlements)\nValid to_status: UNFULFILLED, FULFILLED")
        return {}
    url= f"https://api.twitch.tv/helix/entitlements/drops"
    data={
        "fulfillment_status": to_status,
        "entitlement_ids": entitlement_ids,
    }
    headers_modifier = {
        "Content-Type": "application/json",
    }  
    return await single(channel_id,url,"PATCH",data=data)