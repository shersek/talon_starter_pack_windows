from talon.voice import Context, Key
from talon import ctrl
from ..utils import time_delay

context = Context(
    "GoogleChrome",
    exe="C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe",
)

# def helper(apps , win):
# print(apps , win)
# return False
# context = Context("GoogleChrome", func=helper)

keymap = {
    # navigating the page
    "scroll tiny down": Key("down"),
    "scroll tiny up": Key("up"),
    "(scroll|page) top": Key("q"),
    "(scroll|page) bottom": Key("w"),
    "scroll up": Key("i"),  # already defined in standard.py
    "scroll down": Key("u"),  # already defined in standard.py
    "scroll big down": Key("U"),
    "scroll big up": Key("I"),
    "scroll left": Key("left"),
    "scroll right": Key("right"),
    # change mode
    "insert mode": Key(","),
    "visual mode": Key("."),
    "visual line mode": Key(";"),
    "find mode": Key("/"),
    # copy/paste/select all/refresh
    "steal": Key("ctrl-c"),  # move steal/stick/get all to standard later
    "stick": Key("ctrl-v"),
    "get all": Key("ctrl-a"),
    "refresh": Key("ctrl-r"),
    # opening links
    "open [here]": Key("y"),
    "open new": Key("Y"),
    "open new go": Key("&"),
    "open hide": Key("ctrl-y"),
    "open many": Key("ctrl-7"),
    "done": [Key("escape")] * 2,
    "next page": Key("] ]"),
    "previous page": Key("[ ["),
    "search tabs": Key("\\"),
    # marking
    "mark [this]": Key("1"),
    "go to mark": Key("`"),
    # opening new urls and searching
    "search bar": Key("o"),
    "search bar new": Key("O"),
    # find mode commands
    "(next match | find next)": Key("p"),
    "(previous match | preev match | find previous | find preev)": Key("P"),
    # navigating history
    "history back": Key("h"),
    "history forward": Key("l"),
    # manipulating tabs
    "new tab": Key("m"),
    "lefty tab": [
        Key("j"),
        time_delay(0.2),
    ],  # for repetitive switching delay was necessary
    "righty tab": [
        Key("k"),
        time_delay(0.2),
    ],  # for repetitive switching delay was necessary
    "previous tab": Key("^"),
    "top tab": Key("-"),
    "bottom tab": Key("="),
    "duplicate tab": Key("8"),
    "close tab": Key("n"),
    "restore [tab]": Key("N"),
    "new window": Key("W"),
    "close all left": Key("7"),
    "close all right": Key("9"),
    "close all tabs": Key("0"),
    # chrome functions
    "chrome find": Key("ctrl-f"),
    "chrome close [tab]": Key("ctrl-f4"),
    "chrome restore [tab]": Key("ctrl-shift-t"),
    "chrome right": Key("ctrl-tab"),
    "chrome left": Key("ctrl-shift-tab"),
    "chrome settings": Key("alt-f"),
    "chrome (cast | screen)": [
        Key("alt-f"),
        time_delay(0.2),
        Key("c"),
        time_delay(0.2),
        Key("space"),
    ],
    "chrome print": [Key("ctrl-p"), time_delay(3)] + [Key("tab")] * 2,
    "chrome save": Key("ctrl-s"),
    "chrome downloads": [
        Key("ctrl-j"),
        time_delay(1),
        Key("esc"),
        Key("esc"),
        Key("tab"),
        Key("tab"),
    ],
    "bookmark page": [Key("ctrl-d")] + [Key("tab")] * 3,
    "(chrome | cell | sell | select) address bar": Key("ctrl-l"),
    "copy address [bar]": [
        Key("ctrl-l"),
        time_delay(0.3),
        Key("ctrl-c"),
        time_delay(0.3),
        Key("tab"),
        Key("tab"),
    ],
    "(launch | go to) gmail": [
        Key("shift-o"),
        time_delay(0.5),
        "https://mail.google.com/mail/u/0/#inbox",
        time_delay(0.5),
        Key("enter"),
    ],
    "(launch | go to) [google] drive": [
        Key("shift-o"),
        time_delay(0.5),
        "https://drive.google.com/drive/my-drive",
        time_delay(0.5),
        Key("enter"),
    ],
    # Page cruising not possible currently in windows beta
    # "start (cruz | crews | cruise) [down]": lambda m: ctrl.key_press("down", down=True),
    # "stop (cruz | crews | cruise) [down]": lambda m: ctrl.key_press("down", up=True),
    # "start (cruz | crews | cruise) up": lambda m: ctrl.key_press("up", down=True),
    # "stop (cruz | crews | cruise) up": lambda m: ctrl.key_press("up", up=True),
}

context.keymap(keymap)
