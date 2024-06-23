#from functions.ClassFunctions.user_storrage import ust
import websockets
import json
import os
import re
import requests
import asyncio
from dataclasses import dataclass
from ExtraDecorators import private

event_map = {
    "raw": [], # literally everything that comes in
    "all": [],
    #automod
    "automod.message.hold": [],
    "automod.message.update": [],
    "automod.settings.update": [],
    "automod.therms.update": [],
    #channelupdate
    "channel.update": [],
    #channel.follow
    "channel.follow": [],
    #channel.ad_break
    "channel.ad_break.begin": [],
    #channel.chat
    "channel.chat.message": [],
    "channel.chat.message_delete": [],
    "channel.chat.clear_user_messages": [],
    "channel.chat.clear": [],
    "channel.chat.user_message_update": [],
    "channel.chat.user_message_hold": [],
    "channel.chat_settings.update": [],
    "channel.chat.notification": [],
    #channel.subscription
    "channel.subscribe": [],
    "channel.subscription.end": [],
    "channel.subscription.gift": [],
    "channel.subscription.message": [],
    #channel.cheer
    "channel.cheer": [],
    #channel.raid
    "channel.raid.inbound": [],
    "channel.raid.outbound": [],
    #channel.bans
    "channel.ban": [],
    "channel.unban": [],
    "channel.unban_request.create": [],
    "channel.unban_request.resolve": [],
    #channel.moderate
    "channel.moderate": [],
    #channel.moderator
    "channel.moderator.remove": [],
    "channel.moderator.add": [],
    #channel.guest_star
    "channel.guest_star_session.begin": [],
    "channel.guest_star_session.end": [],
    "channel.guest_star_guest.update": [],
    "channel.guest_star_settings.update": [],
    #channel.points
    "channel.channel_points_automatic_reward_redemption.add": [],
    "channel.channel_points_custom_reward.add": [],
    "channel.channel_points_custom_reward.update": [],
    "channel.channel_points_custom_reward.remove": [],
    "channel.channel_points_custom_reward_redemption.add": [],
    "channel.channel_points_custom_reward_redemption.update": [],
    #channel.poll
    "channel.poll.begin": [],
    "channel.poll.end": {
        "all": [],
        "completed": [],
        "terminated": [],
        "archived": [] 
    },
    "channel.poll.progress": [],
    #channel.prediction
    "channel.prediction.begin": [],
    "channel.prediction.progress": [],
    "channel.prediction.lock": [],
    "channel.prediction.end": {
        "all": [],
        "resolved": [],
        "cancelled": [],
    },
    #channel.suspicous_user
    "channel.suspicous_user.update": [],
    "channel.suspicous_user.message": [],
    #channel.vip
    "channel.vip.add": [],
    "channel.vip.remove": [],
    #channel.hypetrain
    "channel.hypetrain.begin": [],
    "channel.hypetrain.progress": [],
    "channel.hypetrain.end": [],
    #channel.charity
    "channel.charity_campaign.donate": [],
    "channel.charity_campaign.start": [],
    "channel.charity_campaign.progress": [],
    "channel.charity_campaign.stop": [],
    #channel.shield_mode
    "channel.shield_mode.begin": [],
    "channel.shield_mode.end": [],
    #channel.shoutout
    "channel.shoutout.create": [],
    "channel.shoutout.recieve": [],
    #conduit
    "conduit.shard.disabled": [],
    #drop
    "drop.entitlement.grant": [],
    #extension
    "extension.bits_transaction.create": [],
    #goal
    "channel.goal.begin": [],
    "channel.goal.progress": [],
    "channel.goal.end": [],
    #stream
    "stream.online": [],
    "stream.offline": [],
    #authorization
    "user.authorization.grant": [],
    "user.authorization.revoke": [],
    #user
    "user.update": [],
    #whisper
    "user.whisper.message": [],
} 


class twitch:
    _part_of_twitch_event_family = []

    @staticmethod
    def _register_event(event_type, func):
        if func in twitch._part_of_twitch_event_family:
            raise ValueError(f"Function '{func.__name__}' is already decorated with a Twitch event.")
        
        twitch._part_of_twitch_event_family.append(func)
        event_map[event_type].append(func)
        return func

    @staticmethod
    def raw(func):
        return twitch._register_event("raw", func)

    @staticmethod
    def all(func):
        return twitch._register_event("all", func)

    class automod:
        @staticmethod
        def hold(func):
            return twitch._register_event("automod.message.hold", func)

        @staticmethod
        def message_update(func):
            return twitch._register_event("automod.message.update", func)

        @staticmethod
        def settings_update(func):
            return twitch._register_event("automod.settings.update", func)

        @staticmethod
        def therms_update(func):
            return twitch._register_event("automod.therms.update", func)

    @staticmethod
    def channel_update(func):
        return twitch._register_event("channel.update", func)

    @staticmethod
    def follow(func):
        return twitch._register_event("channel.follow", func)

    @staticmethod
    def ad_break_begin(func):
        return twitch._register_event("channel.ad_break.begin", func)

    class chat:
        @staticmethod
        def message(func):
            return twitch._register_event("channel.chat.message", func)

        @staticmethod
        def message_delete(func):
            return twitch._register_event("channel.chat.message_delete", func)

        @staticmethod
        def clear_user_messages(func):
            return twitch._register_event("channel.chat.clear_user_messages", func)

        @staticmethod
        def clear(func):
            return twitch._register_event("channel.chat.clear", func)

        @staticmethod
        def user_message_update(func):
            return twitch._register_event("channel.chat.user_message_update", func)

        @staticmethod
        def user_message_hold(func):
            return twitch._register_event("channel.chat.user_message_hold", func)

        @staticmethod
        def settings_update(func):
            return twitch._register_event("channel.chat_settings.update", func)

        @staticmethod
        def notification(func):
            return twitch._register_event("channel.chat.notification", func)

    class subscription:
        @staticmethod
        def new(func):
            return twitch._register_event("channel.subscribe", func)

        @staticmethod
        def end(func):
            return twitch._register_event("channel.subscription.end", func)

        @staticmethod
        def gift(func):
            return twitch._register_event("channel.subscription.gift", func)

        @staticmethod
        def resub(func):
            return twitch._register_event("channel.subscription.message", func)

    @staticmethod
    def cheer(func):
        return twitch._register_event("channel.cheer", func)

    class raid:
        @staticmethod
        def inbound(func):
            return twitch._register_event("channel.raid.inbound", func)

        @staticmethod
        def outbound(func):
            return twitch._register_event("channel.raid.outbound", func)

    class bans:
        @staticmethod
        def create(func):
            return twitch._register_event("channel.ban", func)

        @staticmethod
        def unban(func):
            return twitch._register_event("channel.unban", func)

        @staticmethod
        def unban_request_create(func):
            return twitch._register_event("channel.unban_request.create", func)

        @staticmethod
        def unban_request_resolve(func):
            return twitch._register_event("channel.unban_request.resolve", func)

    @staticmethod
    def moderate(func):
        return twitch._register_event("channel.moderate", func)

    class moderator:
        @staticmethod
        def remove(func):
            return twitch._register_event("channel.moderator.remove", func)

        @staticmethod
        def add(func):
            return twitch._register_event("channel.moderator.add", func)

    class guest_star:
        @staticmethod
        def session_begin(func):
            return twitch._register_event("channel.guest_star_session.begin", func)

        @staticmethod
        def session_end(func):
            return twitch._register_event("channel.guest_star_session.end", func)

        @staticmethod
        def guest_update(func):
            return twitch._register_event("channel.guest_star_guest.update", func)

        @staticmethod
        def settings_update(func):
            return twitch._register_event("channel.guest_star_settings.update", func)

    class points:
        @staticmethod
        def automatic_reward_redemption_add(func):
            return twitch._register_event("channel.channel_points_automatic_reward_redemption.add", func)

        @staticmethod
        def custom_reward_add(func):
            return twitch._register_event("channel.channel_points_custom_reward.add", func)

        @staticmethod
        def custom_reward_update(func):
            return twitch._register_event("channel.channel_points_custom_reward.update", func)

        @staticmethod
        def custom_reward_remove(func):
            return twitch._register_event("channel.channel_points_custom_reward.remove", func)

        @staticmethod
        def custom_reward_redemption_add(func):
            return twitch._register_event("channel.channel_points_custom_reward_redemption.add", func)

        @staticmethod
        def custom_reward_redemption_update(func):
            return twitch._register_event("channel.channel_points_custom_reward_redemption.update", func)

    class poll:
        @staticmethod
        def begin(func):
            return twitch._register_event("channel.poll.begin", func)

        @staticmethod
        def end(func):
            return twitch._register_event("channel.poll.end.all", func)

        @staticmethod
        def progress(func):
            return twitch._register_event("channel.poll.progress", func)

        @staticmethod
        def completed(func):
            return twitch._register_event("channel.poll.end.completed", func)

        @staticmethod
        def terminated(func):
            return twitch._register_event("channel.poll.end.terminated", func)

        @staticmethod
        def archived(func):
            return twitch._register_event("channel.poll.end.archived", func)

    class prediction:
        @staticmethod
        def begin(func):
            return twitch._register_event("channel.prediction.begin", func)

        @staticmethod
        def progress(func):
            return twitch._register_event("channel.prediction.progress", func)

        @staticmethod
        def lock(func):
            return twitch._register_event("channel.prediction.lock", func)

        @staticmethod
        def end(func):
            return twitch._register_event("channel.prediction.end.all", func)

        @staticmethod
        def resolved(func):
            return twitch._register_event("channel.prediction.end.resolved", func)

        @staticmethod
        def cancelled(func):
            return twitch._register_event("channel.prediction.end.cancelled", func)

    class suspicious_user:
        @staticmethod
        def update(func):
            return twitch._register_event("channel.suspicious_user.update", func)

        @staticmethod
        def message(func):
            return twitch._register_event("channel.suspicious_user.message", func)

    class vip:
        @staticmethod
        def add(func):
            return twitch._register_event("channel.vip.add", func)

        @staticmethod
        def remove(func):
            return twitch._register_event("channel.vip.remove", func)

    class hypetrain:
        @staticmethod
        def begin(func):
            return twitch._register_event("channel.hypetrain.begin", func)

        @staticmethod
        def progress(func):
            return twitch._register_event("channel.hypetrain.progress", func)

        @staticmethod
        def end(func):
            return twitch._register_event("channel.hypetrain.end", func)

    class charity:
        @staticmethod
        def donate(func):
            return twitch._register_event("channel.charity_campaign.donate", func)

        @staticmethod
        def start(func):
            return twitch._register_event("channel.charity_campaign.start", func)

        @staticmethod
        def progress(func):
            return twitch._register_event("channel.charity_campaign.progress", func)

        @staticmethod
        def stop(func):
            return twitch._register_event("channel.charity_campaign.stop", func)

    class shield_mode:
        @staticmethod
        def begin(func):
            return twitch._register_event("channel.shield_mode.begin", func)

        @staticmethod
        def end(func):
            return twitch._register_event("channel.shield_mode.end", func)

    class shoutout:
        @staticmethod
        def create(func):
            return twitch._register_event("channel.shoutout.create", func)

        @staticmethod
        def receive(func):
            return twitch._register_event("channel.shoutout.receive", func)

    class goal:
        @staticmethod
        def begin(func):
            return twitch._register_event("channel.goal.begin", func)

        @staticmethod
        def progress(func):
            return twitch._register_event("channel.goal.progress", func)

        @staticmethod
        def end(func):
            return twitch._register_event("channel.goal.end", func)

    class stream:
        @staticmethod
        def online(func):
            return twitch._register_event("stream.online", func)

        @staticmethod
        def offline(func):
            return twitch._register_event("stream.offline", func)

    @staticmethod
    def user_update(func):
        return twitch._register_event("user.update", func)

    @staticmethod
    def user_whisper_message(func):
        return twitch._register_event("user.whisper.message", func)

@private
@dataclass
class tmp:
    TWITCH_CLIENT_ID: str = None
    TWITCH_ACCESS_TOKEN: str = None
    TWITCH_USER_ID: str = None
    EVENT_SUBSCRIPTION: list = None
    TWITCH_EVENTSUB_TICKET: str = None

tp = tmp()

@private
def on_close(ws, close_status, close_reason):
    print(f"### closed ### {close_reason} code: {close_status}")
 
@private
async def on_message(message):
    MESSAGE = json.loads(message)
    for i in event_map["raw"]:
        await i(MESSAGE)
    if(MESSAGE["metadata"]["message_type"] == "session_welcome"):
        tp.TWITCH_EVENTSUB_TICKET = MESSAGE["payload"]["session"]["id"]
        for i in tp.EVENT_SUBSCRIPTION:
            headers = {
                "Content-Type": "application/json",
                "Client-ID": tp.TWITCH_CLIENT_ID,
                "Authorization": f"Bearer {tp.TWITCH_ACCESS_TOKEN}"
            }
            data = {
                "type": i["type"],
                "version": i["version"],
                "transport": {
                    "method": "websocket",
                    "session_id": tp.TWITCH_EVENTSUB_TICKET
                }
            }
            conditions = i.get("conditions", [])
            if conditions:
                data["condition"] = {}
                for condition in conditions:
                    data["condition"][condition] = tp.TWITCH_USER_ID
            try:
                response = requests.post("https://api.twitch.tv/helix/eventsub/subscriptions", headers=headers, data=json.dumps(data), timeout=5)
                if not response.ok:
                    print(response.json())
            except requests.exceptions.Timeout:
                print("🕒 Twitch: EventSub subscription failed")

        print("### eventsub ready ###")
    

    if(MESSAGE["metadata"]["message_type"] == "notification"):
        for i in event_map["all"]:
            await i(MESSAGE)

        if MESSAGE["metadata"]["subscription_type"] == "channel.raid":
            if MESSAGE["payload"]["subscription"]["to_broadcaster_user_id"]:
                for i in event_map["channel.raid"]["inbound"]:
                    await i(MESSAGE["payload"]["event"])
                    continue
            else:
                for i in event_map["channel.raid"]["outbound"]:
                    await i(MESSAGE["payload"]["event"])
                    continue

        if MESSAGE["metadata"]["subscription_type"] in event_map:
            if isinstance(event_map[MESSAGE["metadata"]["subscription_type"]], list):
                for i in event_map[MESSAGE["metadata"]["subscription_type"]]:
                    await i(MESSAGE["payload"]["event"])
            if isinstance(event_map[MESSAGE["metadata"]["subscription_type"]], dict):
                if event_map[MESSAGE["metadata"]["subscription_type"]][MESSAGE["payload"]["event"]["status"]]:
                    for i in event_map[MESSAGE["metadata"]["subscription_type"]][MESSAGE["payload"]["event"]["status"]]:
                        await i(MESSAGE["payload"]["event"])
                        if event_map[MESSAGE["metadata"]["subscription_type"]]["all"]:
                            for i in event_map[MESSAGE["metadata"]["subscription_type"]]["all"]:
                                await i(MESSAGE["payload"]["event"])
                else:
                    for i in event_map[MESSAGE["metadata"]["subscription_type"]]["fallback"]:
                        await i(MESSAGE["payload"]["event"])
        
        



def initEventSub(userid):
    from RTS_Twitch.overwrites import overwrites
    from RTS_Twitch.memory import memory
    dat = overwrites.get_user(userid)
    tp.TWITCH_ACCESS_TOKEN = dat.get("access_token")
    tp.TWITCH_CLIENT_ID = memory.app_id
    tp.TWITCH_USER_ID = userid
    if not dat.get("event_subscription"):
        overwrites.save_user({"user_id": userid, "event_subscription": memory.event_subscription})
    dat = overwrites.get_user(userid)
    tp.EVENT_SUBSCRIPTION = dat.get("event_subscription")
    
    print("dummy init")
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.create_task(actualInit())
    loop.run_forever()  # Nur wenn Sie möchten, dass der Loop weiterläuft

@private
async def actualInit():
        print("init")
        async with websockets.connect('wss://eventsub.wss.twitch.tv/ws') as ws:
            try:
                while True:
                    message = await ws.recv()
                    await on_message(message)
            except websockets.exceptions.ConnectionClosed as e:
                print("### eventsub closed ###\nStatus: {e.code}\nReason: {e.reason}\n### eventsub closed ###")
            finally:
                await ws.close()



