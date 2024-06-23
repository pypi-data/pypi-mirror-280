from RTS_Twitch.overwrites import overwrites
from RTS_Twitch.memory import memory
import aiohttp
async def paginate(channel_id:int, url:str, methode:str="GET",data:dict={}, headers_modifier:dict={})->dict:
    headers= {
            "Client-ID": memory.app_id,
        }


    if not channel_id is None:
        get_user = overwrites.get_user(channel_id)
        if not get_user:
            return {"error":"User not found.","issue_code":"db_user_not_found"}
        headers["Authorization"] = f"Bearer {get_user['access_token']}"
        
    headers.update(headers_modifier)
    querry = ""
    all_data = []
    async with aiohttp.ClientSession() as session:
        while True:
            if methode == "GET":
                response = await session.get(url + querry, headers=headers,data=data)
            if methode == "POST":
                response = await session.post(url + querry, headers=headers,json=data)
            if methode == "PATCH":
                response = await session.patch(url + querry, headers=headers,json=data)
            if methode == "DELETE":
                response = await session.delete(url + querry, headers=headers)
            else:
                return {"error":"Invalid methode","issue_code":"invalid_methode"}

            data = await response.json()
            if not response.ok:
                return {"error":f"Error in paginate. @toolset.py(paginate)->{response.text}","issue_code":"response_not_ok"}
            all_data.extend(data["data"])
            if "pagination" in data and "cursor" in data["pagination"]:
                if "?" in url:
                    querry = "&after="+data["pagination"]["cursor"]
                else:
                    querry = "?after="+data["pagination"]["cursor"]
            else:
                break
    return all_data

async def single(channel_id:int,url:str,methode:str="GET", headers_modifier:dict={}, data:dict={})->dict:
    get_user = overwrites.get_user(channel_id)
    if not get_user:
        return {"error":"User not found.","issue_code":"db_user_not_found"}
    headers= {
        "Client-ID": memory.app_id,
        "Authorization": f"Bearer {get_user['access_token']}"
    }
    headers.update(headers_modifier)
    async with aiohttp.ClientSession() as session:
        if methode == "GET":
            response = await session.get(url, headers=headers,data=data)
        if methode == "POST":
            response = await session.post(url, headers=headers,json=data)
        if methode == "PATCH":
            response = await session.patch(url, headers=headers,json=data)
        if methode == "DELETE":
            response = await session.delete(url, headers=headers)
            if not response.ok:
                session.close()
                return {"error":f"Error in single_request. @toolset.py(single)->{response.text}", "issue_code":"response_not_ok"}
            session.close()
            return await response.json()
        
        

async def single(channel_id:int,url:str,methode:str="GET", headers_modifier:dict={}, data:dict={})->dict:
    get_user = overwrites.get_user(channel_id)
    if not get_user:
        return {"error":"User not found.","issue_code":"db_user_not_found"}
    headers= {
        "Client-ID": memory.app_id,
        "Authorization": f"Bearer {get_user['access_token']}"
    }
    headers.update(headers_modifier)
    async with aiohttp.ClientSession() as session:
        if methode == "GET":
            response = await session.get(url, headers=headers,data=data)
        if methode == "POST":
            response = await session.post(url, headers=headers,json=data)
        if methode == "PATCH":
            response = await session.patch(url, headers=headers,json=data)
        if methode == "DELETE":
            response = await session.delete(url, headers=headers)
            if not response.ok:
                session.close()
                return {"error":f"Error in single_request. @toolset.py(single)->{response.text}", "issue_code":"response_not_ok"}
            session.close()
            return await response.json()
        
        
