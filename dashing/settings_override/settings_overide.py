from talon import Module, settings
from talon import Context

mod = Module()
ctx = Context()

ctx.matches = r"""
os: windows
os: linux
os: mac
"""


@mod.action_class
class user_actions:

    def clipboard_enable():
        """Enables always clipboard by setting paste threshold to 0"""

        print("threshold was: ", settings.get("user.paste_to_insert_threshold"))

        ctx.settings["user.paste_to_insert_threshold"] = 0

        print("threshold now: ", settings.get("user.paste_to_insert_threshold"))

    def clipboard_disable():
        """ disabled clipboard by setting paste threshold to -1"""

        print("threshold was: ", settings.get("user.paste_to_insert_threshold"))

        ctx.settings["user.paste_to_insert_threshold"] = -1

        print("threshold now: ", settings.get("user.paste_to_insert_threshold"))
