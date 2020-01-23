import time

from talon import ctrl
from talon.voice import Context, Key

from ..utils import text

ctx = Context(
    "Kindle",
    exe="C:\\Users\\herse\\AppData\\Local\\Amazon\\Kindle\\application\\Kindle.exe",
)

keymap = {
    # Anywhere in the application
    "go (home | main | mane)": Key("ctrl-alt-l"),
    "kindle (sink | sync)": Key("f5"),
    # From library
    "sort [by] recent": Key("ctrl-alt-r"),
    "sort [by] title": Key("ctrl-alt-t"),
    "sort [by] author": Key("ctrl-alt-u"),
    # While reading a book
    "[go] (next | neck)": Key("right"),
    "[go] (preev | previous)": Key("left"),
    # Zoom in and zoom out (font size) functions already implemented
    "go (to | location)": Key("ctrl-g"),
    "close book": Key("ctrl-w"),
    "search for": Key("ctrl-f"),
    "[toggle] (full screen | fullscreen)": Key("f11"),
    "single column": Key("alt-1"),
    "(two | double) column": Key("alt-2"),
    "(multi | multiple) column": Key("alt-3"),
    # Using text-to-speech
    "(narrate | read) toggle": Key("ctrl-t"),
    "(narrate | read) (stop | pause)": Key("space"),
    "(narrate | read) (resume | continue | start)": Key("space"),
    "(narrate | read) (previous | preev)": Key("ctrl-shift-up"),
    "(narrate | read) (next | neck)": Key("ctrl-shift-down"),
    # Faster and slower narration does not work
    # Might be because key_press implementation incomplete?
    # "(narrate | read) faster": lambda m: (
    #     ctrl.key_press("shift", shift=True, down=True),
    #     time.sleep(0.1),
    #     ctrl.key_press("=", shift=True, down=True),
    #     time.sleep(0.1),
    #     ctrl.key_press("shift", shift=True, up=True),
    # ),
    # "(narrate | read) slower": lambda m: (
    #     ctrl.key_press("shift", shift=True, down=True),
    #     time.sleep(0.1),
    #     ctrl.key_press("-", shift=True, down=True),
    #     time.sleep(0.1),
    #     ctrl.key_press("shift", shift=True, up=True),
    # ),
}

ctx.keymap(keymap)
