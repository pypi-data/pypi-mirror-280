from __future__ import annotations
from dataclasses import dataclass, field, fields
from typing import Union, Tuple
from RTS_Twitch.Scopes import Scopes
from ExtraUtils.callbackVoid import callbackvoid
from ExtraTypes import snowflake

@dataclass 
class MEMORY():
    app_id: str = None
    app_secret: str = None
    base_url: str = "https://id.twitch.tv/"
    scopes:Scopes = field(default_factory=Scopes)
    ident: int = None
    access_token: str = None
    refresh_token: str = None
    auth_code: str = None
    signed_in: snowflake = False
    multible_users: bool = False
    event_subscription: list = field(default_factory=list)
    session_id: snowflake = str(snowflake())

    @classmethod
    def copy(cls, existing_memory):
        new_memory = cls()
        for f in fields(cls):
            if f.name != 'callback_function':
                setattr(new_memory, f.name, getattr(existing_memory, f.name))
        new_memory.callback_function = existing_memory.callback_function.__func__ if hasattr(existing_memory.callback_function, '__func__') else existing_memory.callback_function
        return new_memory

memory = MEMORY()