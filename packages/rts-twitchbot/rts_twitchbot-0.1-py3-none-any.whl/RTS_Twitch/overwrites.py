from __future__ import annotations
from dataclasses import dataclass, field, fields
from typing import Union, Tuple
from ExtraDecorators import private
from ExtraUtils.callbackVoid import callbackvoid
from RTS_Twitch.Authenticate import load_database, get_user, save_user

@private
@dataclass 
@dataclass
class OVERWRITES():
    functions: dict = None

    def __post_init__(self):
        # Initialisiere das Dictionary mit Standardfunktionen, falls nicht anders angegeben
        if self.functions is None:
            self.functions = {
                "save_user": save_user,
                "login_users": load_database,
                "get_user": get_user,
            }

    def overwrite(self, name, function):
        self.functions[name] = function

    def __getattr__(self, name):
        if name in self.functions:
            def function_wrapper(*args, **kwargs):
                return self.functions[name](*args, **kwargs)
            return function_wrapper
        raise AttributeError(f"'{type(self).__name__}' object has no attribute '{name}'")



overwrites = OVERWRITES()