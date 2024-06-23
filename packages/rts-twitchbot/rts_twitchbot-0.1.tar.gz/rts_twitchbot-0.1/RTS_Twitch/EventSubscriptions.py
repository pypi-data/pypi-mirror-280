
class event_subscriptions():
    def __init__(self):
        self.subs:list = []

    def automod(self):
        self.subs.append({"type": "automod.message.hold","version": "1","conditions": ["broadcaster_user_id","moderator_user_id"]})
        self.subs.append({"type": "automod.message.update","version": "1","conditions": ["broadcaster_user_id","moderator_user_id"]})
        self.subs.append({"type": "automod.settings.update","version": "1","conditions": ["broadcaster_user_id","moderator_user_id"]})
        self.subs.append({"type": "automod.therms.update","version": "1","conditions": ["broadcaster_user_id","moderator_user_id"]})

    def channel_update(self):
        self.subs.append({"type": "channel.update","version": "2","conditions": ["broadcaster_user_id"]})

    def channel_follow(self):
        self.subs.append({"type": "channel.follow","version": "2","conditions": ["broadcaster_user_id","moderator_user_id"]})

    def channel_ad_break_begin(self):
        self.subs.append({"type": "channel.ad_break.begin","version": "1","conditions": ["broadcaster_user_id"]})

    def channel_chat_manage(self):
        self.subs.append({"type": "channel.chat.message","version": "1","conditions": ["broadcaster_user_id","user_id"]})
        self.subs.append({"type": "channel.chat.message_delete","version": "1","conditions": ["broadcaster_user_id","user_id"]})
        self.subs.append({"type": "channel.chat.clear_user_messages","version": "1","conditions": ["broadcaster_user_id","user_id"]})
        self.subs.append({"type": "channel.chat.clear","version": "1","conditions": ["broadcaster_user_id","user_id"]})
        self.subs.append({"type": "channel.chat.user_message_update","version": "1","conditions": ["broadcaster_user_id","user_id"]})
        self.subs.append({"type": "channel.chat.user_message_hold","version": "1","conditions": ["broadcaster_user_id","user_id"]})
        self.subs.append({"type": "channel.chat_settings.update","version": "1","conditions": ["broadcaster_user_id","user_id"]})
        self.subs.append({"type": "channel.chat.notification","version": "1","conditions": ["broadcaster_user_id","user_id"]})

    def channel_subscriptions(self):
        self.subs.append({"type": "channel.subscribe","version": "1","conditions": ["broadcaster_user_id"]})
        self.subs.append({"type": "channel.subscription.end","version": "1","conditions": ["broadcaster_user_id"]})
        self.subs.append({"type": "channel.subscription.gift","version": "1","conditions": ["broadcaster_user_id"]})
        self.subs.append({"type": "channel.subscription.message","version": "1","conditions": ["broadcaster_user_id"]})


    def channel_cheer(self):
        self.subs.append({"type": "channel.cheer","version": "1","conditions": ["broadcaster_user_id"]})

    def channel_raid(self):
        self.subs.append({"type": "channel.raid","version": "1","conditions": ["from_broadcaster_user_id"]})
        self.subs.append({"type": "channel.raid","version": "1","conditions": ["to_broadcaster_user_id"]})

    def channel_bans(self):
        self.subs.append({"type": "channel.ban","version": "1","conditions": ["broadcaster_user_id"]})
        self.subs.append({"type": "channel.unban","version": "1","conditions": ["broadcaster_user_id"]})
        self.subs.append({"type": "channel.unban_request.create","version": "1","conditions": ["broadcaster_user_id","moderator_user_id"]})
        self.subs.append({"type": "channel.unban_request.resolve","version": "1","conditions": ["broadcaster_user_id","moderator_user_id"]})
      

    def channel_moderate(self):
        self.subs.append({"type": "channel.moderate","version": "1","conditions": ["broadcaster_user_id","moderator_user_id"]})

    def channel_moderator(self):
        self.subs.append({"type": "channel.moderator.remove","version": "1","conditions": ["broadcaster_user_id"]})
        self.subs.append({"type": "channel.moderator.add","version": "1","conditions": ["broadcaster_user_id"]})

    def channel_guest_star(self):
        self.subs.append({"type": "channel.guest_star_session.begin","version": "beta","conditions": ["broadcaster_user_id","moderator_user_id"]})
        self.subs.append({"type": "channel.guest_star_session.end","version": "beta","conditions": ["broadcaster_user_id","moderator_user_id"]})
        self.subs.append({"type": "channel.guest_star_guest.update","version": "beta","conditions": ["broadcaster_user_id","moderator_user_id"]})
        self.subs.append({"type": "channel.guest_star_settings.update","version": "beta","conditions": ["broadcaster_user_id","moderator_user_id"]})

    def channel_points(self):
        self.subs.append({"type": "channel.channel_points_automatic_reward_redemption.add","version": "1","conditions": ["broadcaster_user_id"]})
        self.subs.append({"type": "channel.channel_points_custom_reward.add","version": "1","conditions": ["broadcaster_user_id"]})
        self.subs.append({"type": "channel.channel_points_custom_reward.update","version": "1","conditions": ["broadcaster_user_id","reward_id"]})
        self.subs.append({"type": "channel.channel_points_custom_reward.remove","version": "1","conditions": ["broadcaster_user_id","reward_id"]})
        self.subs.append({"type": "channel.channel_points_custom_reward_redemption.add","version": "1","conditions": ["broadcaster_user_id"]})
        self.subs.append({"type": "channel.channel_points_custom_reward_redemption.update","version": "1","conditions": ["broadcaster_user_id"]})

    def channel_poll(self):
        self.subs.append({"type": "channel.poll.begin","version": "1","conditions": ["broadcaster_user_id"]})
        self.subs.append({"type": "channel.poll.end","version": "1","conditions": ["broadcaster_user_id"]})
        self.subs.append({"type": "channel.poll.progress","version": "1","conditions": ["broadcaster_user_id"]})


    def channel_prediction(self):
        self.subs.append({"type": "channel.prediction.begin","version": "1","conditions": ["broadcaster_user_id"]})
        self.subs.append({"type": "channel.prediction.progress","version": "1","conditions": ["broadcaster_user_id"]})
        self.subs.append({"type": "channel.prediction.lock","version": "1","conditions": ["broadcaster_user_id"]})
        self.subs.append({"type": "channel.prediction.end","version": "1","conditions": ["broadcaster_user_id"]})

    def channel_suspicous_user(self):
        self.subs.append({"type": "channel.suspicous_user.update","version": "1","conditions": ["broadcaster_user_id","moderator_user_id"]})
        self.subs.append({"type": "channel.suspicous_user.message","version": "1","conditions": ["broadcaster_user_id","moderator_user_id"]})

    def channel_vip(self):
        self.subs.append({"type": "channel.vip.add","version": "1","conditions": ["broadcaster_user_id"]})
        self.subs.append({"type": "channel.vip.remove","version": "1","conditions": ["broadcaster_user_id"]})

    def channel_hypetrain(self):
        self.subs.append({"type": "channel.hypetrain.begin","version": "1","conditions": ["broadcaster_user_id"]})
        self.subs.append({"type": "channel.hypetrain.progress","version": "1","conditions": ["broadcaster_user_id"]})
        self.subs.append({"type": "channel.hypetrain.end","version": "1","conditions": ["broadcaster_user_id"]})

    def channel_charity(self):
        self.subs.append({"type": "channel.charity_campaign.donate","version": "1","conditions": ["broadcaster_user_id"]})
        self.subs.append({"type": "channel.charity_campaign.start","version": "1","conditions": ["broadcaster_user_id"]})
        self.subs.append({"type": "channel.charity_campaign.progress","version": "1","conditions": ["broadcaster_user_id"]})
        self.subs.append({"type": "channel.charity_campaign.stop","version": "1","conditions": ["broadcaster_user_id"]})

    def channel_shield_mode(self):
        self.subs.append({"type": "channel.shield_mode.begin","version": "1","conditions": ["broadcaster_user_id","moderator_user_id"]})
        self.subs.append({"type": "channel.shield_mode.end","version": "1","conditions": ["broadcaster_user_id","moderator_user_id"]})

    def channel_shoutout(self):
        self.subs.append({"type": "channel.shoutout.create","version": "1","conditions": ["broadcaster_user_id","moderator_user_id"]})
        self.subs.append({"type": "channel.shoutout.recieve","version": "1","conditions": ["broadcaster_user_id","moderator_user_id"]})

    #def conduit_shard_disabled(self):
    #    self.subs.append({"type": "conduit.shard.disabled","version": "1","conditions": ["client_id"]})
#
    #def drop_entitlement_grant(self):
    #    self.subs.append({"type": "drop.entitlement.grant","version": "1","conditions": ["organization_id"]})

    #def extension_bits_transaction_create(self):
    #    self.subs.append({"type": "extension.bits_transaction.create","version": "1","conditions": ["extension_client_id"]})

    def channel_goal(self):
        self.subs.append({"type": "channel.goal.begin","version": "1","conditions": ["broadcaster_user_id"]})
        self.subs.append({"type": "channel.goal.progress","version": "1","conditions": ["broadcaster_user_id"]})
        self.subs.append({"type": "channel.goal.end","version": "1","conditions": ["broadcaster_user_id"]})

    def stream(self):
        self.subs.append({"type": "stream.online","version": "1","conditions": ["broadcaster_user_id"]})
        self.subs.append({"type": "stream.offline","version": "1","conditions": ["broadcaster_user_id"]})

    #def user_authorization(self):
    #    self.subs.append({"type": "user.authorization.grant","version": "1","conditions": ["client_id"]})
    #    self.subs.append({"type": "user.authorization.revoke","version": "1","conditions": ["client_id"]})

    def user_update(self):
        self.subs.append({"type": "user.update","version": "1","conditions": ["user_id"]})

    def user_whisper_message(self):
        self.subs.append({"type": "user.whisper.message","version": "1","conditions": ["user_id"]})