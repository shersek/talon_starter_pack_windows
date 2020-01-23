import os

from talon import ctrl, tap, ui
from talon.voice import Context, Key

from ..utils import key_pressify_string, text, time_delay

ctx = Context(
    "windows_explorer", func=lambda app, win: app.name.lower() == "windows explorer"
)


def left_right_click_southeast(m):
    win = ui.active_window()
    rect = win.rect
    center_x = rect.x + rect.width / 2
    center_y = rect.y + rect.height / 2
    multiplier = 1.7
    pos = (
        center_x + multiplier * rect.width / 4,
        center_y + multiplier * rect.height / 4,
    )
    ctrl.mouse_move(*pos)
    ctrl.mouse_click(button=0, times=1, wait=16000)
    ctrl.mouse_click(button=1, times=1, wait=16000)


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
    "copy address [bar]": [
        Key("alt-d"),
        time_delay(0.3),
        Key("ctrl-a"),
        time_delay(0.3),
        Key("ctrl-c"),
        time_delay(0.3),
        Key("esc"),
        Key("esc"),
    ],
    "open (get | git) (bash | here)": [left_right_click_southeast]
    + [Key("g"), time_delay(0.1), Key("down"), time_delay(0.1), Key("enter")],
}

ctx.keymap(keymap)
