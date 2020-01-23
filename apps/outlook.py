from talon.voice import Context, Key
from talon import ctrl
from ..utils import text
from ..utils import time_delay
import time

ctx = Context(
    "Outlook", exe="C:\\Program Files\\Microsoft Office\\root\\Office16\\OUTLOOK.EXE"
)

keymap = {
    "reply (message | mail | male)": [
        Key("alt-h"),
        time_delay(0.1),
        Key("r"),
        time_delay(0.1),
        Key("p"),
    ],
    "send (message | mail | male)": Key("ctrl-enter"),
    "next (pain | pane)": Key("ctrl-tab"),
    "preev (pain | pane)": Key("shift-ctrl-tab"),
    "[show] options": lambda m: (
        ctrl.key_press("alt", alt=True, down=True),
        time.sleep(0.5),
        ctrl.key_press("alt", alt=True, up=True),
    ),
    "search bar": Key("ctrl-e"),
    "go inbox": Key("ctrl-shift-i"),
    "compose [message]": Key("ctrl-shift-m"),
    # "dismiss outlook": [lambda m: switch_app(name="outlook"), Key("cmd-w")],
}

ctx.keymap(keymap)
