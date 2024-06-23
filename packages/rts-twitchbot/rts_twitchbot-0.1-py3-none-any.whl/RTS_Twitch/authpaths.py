from aiohttp import web
from RTS_Twitch.memory import memory
from RTS_WebUIBuilder.cache import rtswuib_cache
from RTS_Twitch.overwrites import overwrites
import json

def loadPaths():
    loginpath()
    twitchpath()

def loginpath():
    from RTS_Twitch.Authenticate import trade_code
    async def login(request):
        raise web.HTTPFound(await trade_code(request.query.get("code")))
    rtswuib_cache.MAIN_WEBSERVER.add(method="GET",path="/oauth/twitch/login", handler=login)
    rtswuib_cache.MAIN_WEBSERVER.add(method="GET",path="/oauth/twitch/login/", handler=login)

def twitchpath():
    from RTS_Twitch.Authenticate import signin, first_oauth
    async def twitch(request):
        userid = request.match_info.get("user")
        if not userid:
            redirect = await first_oauth()
            raise web.HTTPFound(redirect)
        print("twitchpath",userid)

        if userid and overwrites.get_user(userid).get("session_id") == memory.session_id:
            return web.Response(text="You are signed in! You can now use the API.")

        redirect = await signin(datasetin=overwrites.get_user(userid))
        raise web.HTTPFound(redirect)
    rtswuib_cache.MAIN_WEBSERVER.add(method="GET",path="/twitch", handler=twitch)
    rtswuib_cache.MAIN_WEBSERVER.add(method="GET",path="/twitch/{user:.*}", handler=twitch)