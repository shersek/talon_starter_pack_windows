import time
from talon.voice import Context, Key, press
from talon import ctrl
from ...utils import time_delay

def helper(app,win):
    # print(win.title.lower().find("leetcode - google chrome")>0)
    return win.title.lower().find("leetcode - google chrome")>0

ctx = Context("overleaf", func=helper)

ctx.keymap(
{
    "run code": Key("ctrl-'")
    }
)
