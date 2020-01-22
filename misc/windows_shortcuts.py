from talon.voice import Context, Key, press
from ..utils import time_delay
from talon import ui

context = Context("windows_shortcuts")

# def ctrl_alt_hold(m):
#     # def internal(m):
#     ctrl.key_press("alt", down=True)
#     # ctrl.key_press("ctrl", down=True)
#     time_delay(0.1)
#     print("here")
#     press("ctrl-delete")
#     ctrl.key_press("alt", up=True)
#     # ctrl.key_press("ctrl", up=True)
#     # return internal
#
# def ctrl_alt_release(m):
#     # def internal(m):
#     ctrl.key_press("alt", up=True)
#     ctrl.key_press("ctrl", up=True)
#     # return internal

keymap = {
    # windows menu/search bar/windows run
    "(win|windows) menu": [Key("win"), time_delay(0.2), Key("tab")],
    "(win|windows) search [bar]": Key("win-s"),
    "(win | windows) run": Key("win-r"),
    "(win|windows) (activities | actions)": Key("win-b"),
    # window manipulation
    "windy up": Key("win-up"),
    "windy down": Key("win-down"),
    "windy left": Key("win-left"),
    "windy right": Key("win-right"),
    "windy screen": Key("win-shift-left"),
    # window switching
    "swank": Key("alt-tab"),
    "(view | show) swank": Key("ctrl-alt-tab"),
    # other shortcuts
    "toggle (dektop|desk)": Key("win-d"),
    "windows (explore|explorer)": Key("win-e"),
    "windows settings": Key("win-i"),
    "take screenshot": Key("win-shift-s"),
    "clip history": Key("win-v"),
    "(view | show) (task|tasks)": Key("win-tab"),
    "(manage tasks | view task manager)": Key("ctrl-shift-escape"),
    "exit (program | window)": Key("alt-f4"),
}

# opening programs on the taskbar
open_taskbar = {"launch task %s" % str(i): Key("win-%s" % str(i)) for i in range(1, 10)}
open_taskbar_new = {
    "launch new task %s" % str(i): Key("win-shift-%s" % str(i)) for i in range(1, 10)
}

keymap.update(open_taskbar)
keymap.update(open_taskbar_new)
context.keymap(keymap)
