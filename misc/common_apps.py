from talon.voice import Context, Key, press
from ..utils import time_delay
from talon import ui

context = Context("common_apps")

keymap = {
    "launch chrome": lambda m: ui.launch(
        path="C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
    ),
    "launch pycharm": lambda m: ui.launch(
        path="C:\\Users\\herse\\AppData\\Local\\JetBrains\\PyCharm Community Edition 2019.2.3\\bin\\pycharm64.exe"
    ),
    "launch slack": lambda m: ui.launch(
        path="C:\\Users\\herse\\AppData\\Local\\slack\\app-4.2.0\\slack.exe"
    ),
    "launch vim": lambda m: ui.launch(
        path="C:\\Program Files (x86)\\Vim\\vim82\\gvim.exe"
    ),
    "launch (notepad | note pad)": lambda m: ui.launch(
        path="C:\\WINDOWS\\system32\\notepad.exe"
    ),
    "launch outlook": lambda m: ui.launch(
        path="C:\\Program Files\\Microsoft Office\\root\\Office16\\OUTLOOK.EXE"
    ),
    "launch (atom | adam)": lambda m: ui.launch(
        path="C:\\Users\\herse\\AppData\\Local\\atom\\app-1.42.0\\atom.exe"
    ),
    "launch kindle": lambda m: ui.launch(
        path="C:\\Users\\herse\\AppData\\Local\\Amazon\\Kindle\\application\\Kindle.exe"
    ),
    "launch paint": lambda m: ui.launch(path="C:\\WINDOWS\\system32\\mspaint.exe"),
    # "launch dropbox": lambda m: ui.launch(path="C:\\Program Files (x86)\\Dropbox\\Client\\Dropbox.exe"), #doesn't work...
    "launch (win | windows) explorer": lambda m: ui.launch(
        path="C:\\WINDOWS\\Explorer.EXE"
    ),
    "launch talon scripts": [
        lambda m: ui.launch(path="C:\\WINDOWS\\Explorer.EXE"),
        time_delay(0.5),
        Key("alt-d"),
        time_delay(0.5),
        "C:\\Users\\herse\\AppData\\Roaming\\talon\\user\\talon_starter_pack_windows",
        time_delay(0.5),
        Key("enter"),
    ],
    "launch bash 1": [
        Key("win-r"),
        time_delay(0.5),
        "bash",
        time_delay(0.5),
        Key("enter"),
    ],
    "launch bash 2": [
        Key("win-r"),
        time_delay(0.5),
        "ubuntu",
        time_delay(0.5),
        Key("enter"),
    ],
    "launch (command | commandline | command line)": [
        Key("win-s"),
        time_delay(0.5),
        "cmd",
        time_delay(0.5),
        Key("enter"),
    ],
    "launch (get | git) bash": [
        Key("win-s"),
        time_delay(0.5),
        "git bash",
        time_delay(0.5),
        Key("enter"),
    ],
}

context.keymap(keymap)
