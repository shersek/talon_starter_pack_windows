from talon.voice import Context, Key
from ..utils import text, key_pressify_string, time_delay
import os

ctx = Context(
    "windows_explorer", func=lambda app, win: app.name.lower() == "windows explorer"
)

keymap = {
    "(select | sell | cell) adress bar": Key("alt-d"),
    "(select | sell | cell) search bar": Key("ctrl-f"),
    "new window": Key("ctrl-n"),
    "close window": Key("ctrl-w"),
    "(show | open | see | view) properties": Key("alt-enter"),
    "history back": Key("alt-left"),
    "history forward": Key("alt-right"),
    "(open | see | view) parent": Key("alt-up"),
    "done": [Key("esc"), Key("tab")] * 2,
    # backspace view the previous folder is already implemented as a "delete" command in basics
    "(talent | talon) adress": Key(
        key_pressify_string(
            "C:\\Users\\herse\\AppData\\Roaming\\talon\\user\\talon_starter_pack_windows"
        )
    ),
    "open with adam": [Key("shift-f10"), time_delay(0.2)]
    + [Key("down")] * 3
    + [time_delay(0.5), Key("enter")],
    "copy address": [
        Key("alt-d"),
        time_delay(0.3),
        Key("ctrl-a"),
        time_delay(0.3),
        Key("ctrl-c"),
        time_delay(0.3),
        Key("esc"),
        Key("esc"),
    ],
}

ctx.keymap(keymap)
