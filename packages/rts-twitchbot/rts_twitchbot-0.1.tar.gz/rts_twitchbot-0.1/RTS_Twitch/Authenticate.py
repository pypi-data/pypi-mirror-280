from RTS_Twitch.memory import MEMORY, memory
from RTS_WebUIBuilder import cache
from RTS_Twitch.Scopes import Scopes	
import aiohttp, asyncio
from aiohttp import web
from RTS_WebUIBuilder.cache import rtswuib_cache as rt
from RTS_Twitch.EventSub import initEventSub
from RTSDataBase.exceptions import *
import traceback

import threading
from RTSDataBase.RTSDB import DB

async def signin(datasetin:dict=None):
    from RTS_Twitch.overwrites import overwrites
    if datasetin is None or not datasetin:
        return await first_oauth()
    if not datasetin.get("access_token"):
        return await refresh(datasetin)
    
    try:
        headers = {
            "Authorization": "Bearer "+ datasetin["access_token"]
        }
        
        async with aiohttp.ClientSession(timeout=aiohttp.ClientTimeout(10)) as session:
            async with session.get(f"https://id.twitch.tv/oauth2/validate", headers=headers) as response:
                if response.ok:
                    response = await response.json()
                    if overwrites.get_user(response["user_id"]).get("session_id") == memory.session_id:
                        return "/twitch/" + response["user_id"]
                    print("Signed in")
                    dataset = {
                        "user_id": response["user_id"],
                        "loginname": response["login"],
                        "session_id": memory.session_id,
                        "access_token": datasetin["access_token"],
                        "refresh_token": datasetin["refresh_token"]
                    }
                    overwrites.save_user(dataset)
                    # file deepcode ignore MissingAPI: juckt keinen
                    thread = threading.Thread(target=initEventSub,args=(response["user_id"],))
                    thread.daemon = True
                    thread.start()
                    return "/twitch/" + response["user_id"]
    except FieldsNotInHeader as e:
        print(e)
        raise

    except Exception as e:
        traceback.print_exc()
        print(e)
    return await refresh(datasetin)
            
async def refresh(datasetin):
    from RTS_Twitch.overwrites import overwrites
    if not datasetin.get("refresh_token"):
        return await first_oauth()

    try:
        headers = {
            "Content-Type": "application/x-www-form-urlencoded"
        }
        data = {
            "grant_type": "refresh_token",
            "refresh_token": datasetin.get("refresh_token"),
            "client_id": memory.app_id,
            "client_secret": memory.app_secret
        }
        async with aiohttp.ClientSession(timeout=aiohttp.ClientTimeout(10)) as session:
            async with session.post(f"https://id.twitch.tv/oauth2/token", headers=headers, data=data) as response:
                if response.ok:
                    response = await response.json()
                    dataset = {
                        "access_token": response["access_token"],
                        "refresh_token": response["refresh_token"],
                    }
                    return await signin(dataset)
    except Exception as e:
        traceback.print_exc()
        print(e)
    return await first_oauth()

async def first_oauth():
    if not memory.scopes:
        raise Exception("Scopes are not set. Can not create first_oauth request without permition scopes.")
    return f"{memory.base_url}oauth2/authorize?client_id={memory.app_id}&redirect_uri=http://localhost:{rt.MAIN_WEBSERVER.port}/oauth/twitch/login&response_type=code&scope={str(memory.scopes)}"

async def trade_code(auth_code:str):

    try:
        headers = {
            "Content-Type": "application/x-www-form-urlencoded"
        }
        data = {
            "client_id": memory.app_id,
            "client_secret": memory.app_secret,
            "code": auth_code,
            "grant_type": "authorization_code",
            "redirect_uri": f"http://localhost:{rt.MAIN_WEBSERVER.port}/oauth/twitch/login"
        }
        async with aiohttp.ClientSession(timeout=aiohttp.ClientTimeout(10)) as session:
            async with session.post(f"https://id.twitch.tv/oauth2/token", headers=headers, data=data) as response:
                if response.ok:
                    response = await response.json()
                    dataset = {
                        "access_token": response["access_token"],
                        "refresh_token": response["refresh_token"]
                    }
                    return await signin(dataset)
    except Exception as e:	
        traceback.print_exc()
        print(e)
    return await first_oauth()


async def load_database():
    db = DB("login")
    db.setHeader({
        "fields": ["user_id","access_token", "refresh_token","event_subscription", "session_id"],
        "format": ["str",    "nostr",        "nostr",        "list",               "nostr"],
        "states": ["unique", "modular",      "modular",      "modular",            "modular"]
    })
    if db.formated_dump():
        for user in db.formated_dump():
            await signin(datasetin=user)

def get_user(userid) -> dict:
    db = DB("login")
    if not db.find(str(userid), "user_id"):
        db.create({
            "user_id": str(userid),
            "access_token": None,
            "refresh_token": None,
            "event_subscription": [],
            "session_id": None
        })

    return db.find(str(userid), "user_id")[0]

def save_user(user):
    db = DB("login")
        
    if not db.find(str(user["user_id"]), "user_id"):
        db.create({
            "user_id": str(user["user_id"]),
            "access_token": None,
            "refresh_token": None,
            "event_subscription": [],
            "session_id": None,
        })
    if user.get("access_token"):
        db.update({"user_id": user["user_id"]}, "access_token", user["access_token"])
    if user.get("refresh_token"):
        db.update({"user_id": user["user_id"]}, "refresh_token", user["refresh_token"])
    if user.get("event_subscription"):
        db.update({"user_id": user["user_id"]}, "event_subscription", user["event_subscription"])
    if user.get("session_id"):
        db.update({"user_id": user["user_id"]}, "session_id", user["session_id"])
