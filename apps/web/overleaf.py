import time
from talon.voice import Context, Key, press
from talon import ctrl
from ...utils import time_delay

def helper(app,win):
    # print(win.title.lower().find("online latex editor overleaf - google chrome")>0)
    return win.title.lower().find("online latex editor overleaf - google chrome")>0

ctx = Context("overleaf", func=helper)

ctx.keymap(
{
    "compile": Key("ctrl-enter"),
    "next error": Key("alt-e"),
    "(preev|previous) error": Key("alt-shift-e"),
    "auto complete": Key("ctrl-space"),
    "bold": Key("ctrl-b"),
    "italic": Key("ctrl-i"),
    }
)
