from urllib.parse import quote_plus

class Scopes:
    def __init__(self):
        self.scopes = set()

    def analytics_read_extensions(self):
        self.scopes.add("analytics:read:extensions")
    
    def analytics_read_games(self):
        self.scopes.add("analytics:read:games")
    
    def bits_read(self):
        self.scopes.add("bits:read")

    def user_read_chat(self):
        self.scopes.add("user:read:chat")

    def user_bot(self):
        self.scopes.add("user:bot") 

    def channel_bot(self):
        self.scopes.add("channel:bot")
    
    def channel_manage_ads(self):
        self.scopes.add("channel:manage:ads")

    def moderation_manage(self):
        self.scopes.add("channel:moderate")
        self.scopes.add("moderator:manage:banned_users")
        self.scopes.add("moderator:manage:automod")
        self.scopes.add("moderator:manage:guest_star")
        self.scopes.add("moderator:manage:chat_messages")
        self.scopes.add("moderator:manage:blocked_terms")
        self.scopes.add("moderator:manage:shoutouts")
        self.scopes.add("moderator:manage:unban_requests")
        self.scopes.add("moderator:manage:shield_mode")
        self.scopes.add("moderator:manage:announcements")

    def moderation_read(self):
        self.scopes.add("moderator:read")
        self.scopes.add("moderator:read:guest_star")
        self.scopes.add("moderator:read:shield_mode")
        self.scopes.add("moderator:read:blocked_terms")
        self.scopes.add("moderator:read:chatters")
        self.scopes.add("moderator:read:chat_messages")
        self.scopes.add("moderator:read:unban_requests")
        self.scopes.add("moderator:read:shoutouts")

    def moderation_read_folowers(self):
        self.scopes.add("moderator:read:followers")
    
    def channel_manage_broadcast(self):
        self.scopes.add("channel:manage:broadcast")
    
    def channel_read_charity(self):
        self.scopes.add("channel:read:charity")

    def channel_edit_commercial(self):
        self.scopes.add("channel:edit:commercial")

    def channel_read_editors(self):
        self.scopes.add("channel:read:editors")

    def channel_manage_extensions(self):
        self.scopes.add("channel:manage:extensions")

    def channel_read_goals(self):
        self.scopes.add("channel:read:goals")

    def channel_read_guest_star(self):
        self.scopes.add("channel:read:guest_star")

    def channel_manage_guest_star(self):
        self.scopes.add("channel:manage:guest_star")

    def channel_read_hype_train(self):
        self.scopes.add("channel:read:hype_train")
    
    def channel_read_hype_train(self):
        self.scopes.add("channel:read:hype_train")

    def channel_manage_modertors(self):
        self.scopes.add("channel:manage:moderators")

    def channel_read_polls(self):
        self.scopes.add("channel:read:polls")

    def channel_manage_polls(self):
        self.scopes.add("channel:manage:polls")

    def channel_read_predictions(self):
        self.scopes.add("channel:read:predictions")

    def channel_manage_predictions(self):
        self.scopes.add("channel:manage:predictions")

    def channel_manage_raids(self):
        self.scopes.add("channel:manage:raids")

    def channel_read_redemptions(self):
        self.scopes.add("channel:read:redemptions")

    def channel_manage_redemptions(self):
        self.scopes.add("channel:manage:redemptions")

    def channel_manage_schedule(self):
        self.scopes.add("channel:manage:schedule")

    def channel_read_stream_key(self):
        self.scopes.add("channel:read:stream_key")

    def channel_read_subscriptions(self):
        self.scopes.add("channel:read:subscriptions")

    def channel_manage_videos(self):
        self.scopes.add("channel:manage:videos")

    def channel_read_vips(self):
        self.scopes.add("channel:read:vips")

    def channel_manage_vips(self):
        self.scopes.add("channel:manage:vips")

    def clips_edit(self):
        self.scopes.add("clips:edit")

    def user_edit(self):
        self.scopes.add("user:edit")

    def user_edit_follows(self):
        self.scopes.add("user:edit:follows")

    def user_read_blocked_users(self):
        self.scopes.add("user:read:blocked_users")

    def user_manage_blocked_users(self):
        self.scopes.add("user:manage:blocked_users")

    def user_read_broadcast(self):
        self.scopes.add("user:read:broadcast")

    def user_manage_chat_color(self):
        self.scopes.add("user:manage:chat_color")

    def user_read_email(self):
        self.scopes.add("user:read:email")

    def user_read_emotes(self):
        self.scopes.add("user:read:emotes")

    def user_read_follows(self):
        self.scopes.add("user:read:follows")

    def user_read_moderated_channels(self):
        self.scopes.add("user:read:moderated_channels")

    def user_read_subscriptions(self):
        self.scopes.add("user:read:subscriptions")

    def user_manage_whispers(self):
        self.scopes.add("user:manage:whispers")


    def __str__(self) -> str:
        string = " ".join(self.scopes)
        return quote_plus(string)