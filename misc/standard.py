from talon.voice import Word, Context, Key, Str, press
from talon import app, clip, ui, ctrl
from talon_init import TALON_HOME, TALON_PLUGINS, TALON_USER
import string
from ..utils import (
    surround,
    parse_words,
    parse_word,
    sentence_text,
    text,
    word,
    time_delay,
    key_pressify_string,
    join_words,
    insert,
)
from talon.engine import engine


def engine_update(j):
    engine.cmd("g.update", name="dragon", enabled=False)


engine.register("ready", engine_update)


def copy_bundle(m):
    bundle = ui.active_app().bundle
    clip.set(bundle)
    app.notify("Copied app bundle", body="{}".format(bundle))


def inputs_vocab(m):
    insert(join_words(m._words))


# def alt_tab_hold():
#     def internal(m):
#         ctrl.key_press("alt", down=True)
#         ctrl.key_press("tab")
#     return internal
#
# def alt_relase():
#     def internal(m):
#         ctrl.key_press("alt", up=True)
#     return internal

ctx = Context("standard")

vocab = [
    "docker",
    "talon",
    "pragma",
    "pragmas",
    "vim",
    "config",
    "configs",
    "spotify",
    "upsert",
    "utils",
    "linux",
    "ubuntu",
]

keymap = {}
keymap.update(
    {
        "dragon words": "<dgnwords>",
        "dragon dictation": "<dgndictation>",
        "slap": [Key("end"), Key("enter")],
        "cd": "cd ",
        "cd talon home": "cd {}\n".format(TALON_HOME),
        "cd talon user": "cd {}\n".format(TALON_USER),
        "cd talon [user] emily": "cd {}/emily\n".format(TALON_USER),
        "cd talon plugins": "cd {}\n".format(TALON_PLUGINS),
        "talon logs": "cd {} && tail -f talon.log\n".format(TALON_HOME),
        "grep": "grep ",
        "(elle less | ellis | ls | LS)": "ls ",
        "run L S": "ls\n",
        "run (S S H | S H)": "ssh",
        "(ssh | sh)": "ssh ",
        "ack": "ack ",
        "diff": "diff ",
        "dot pie": ".py",
        "run vim": "vim ",
        "run make": "make\n",
        "run jobs": "jobs\n",
        "run make (durr | dear)": "mkdir ",
        "(jay son | jason )": "json",
        "(http | htp)": "http",
        "tls": "tls",
        "md5": "md5",
        "(regex | rejex)": "regex",
        "const": "const ",
        "static": "static ",
        "tip pent": "int ",
        "tip char": "char ",
        "tip byte": "byte ",
        "tip pent 64": "int64_t ",
        "tip you went 64": "uint64_t ",
        "tip pent 32": "int32_t ",
        "tip you went 32": "uint32_t ",
        "tip pent 16": "int16_t ",
        "tip you went 16": "uint16_t ",
        "tip pent 8": "int8_t ",
        "tip you went 8": "uint8_t ",
        "tip size": "size_t",
        "tip float": "float ",
        "tip double": "double ",
        "args": ["()", Key("left")],
        "[inside] (index | array)": ["[]", Key("left")],
        "block": ["{}", Key("left enter enter up tab")],
        "empty array": "[]",
        "comment see": "// ",
        "word queue": "queue",
        "word eye": "eye",
        "word bson": "bson",
        "word iter": "iter",
        "word no": "NULL",
        "word cmd": "cmd",
        "word dup": "dup",
        "word streak": ["streq()", Key("left")],
        "word printf": "printf",
        "word shell": "shell",
        "word Point2d": "Point2d",
        "word Point3d": "Point3d",
        "title Point": "Point",
        "word angle": "angle",
        "dunder in it": "__init__",
        "self taught": "self.",
        "(dickt in it | inside bracket | in bracket)": ["{}", Key("left")],
        "(in | inside) percent": ["%%", Key("left")],
        "list in it": ["[]", Key("left")],
        "string utf8": "'utf8'",
        "state past": "pass",
        "shebang bash": "#!/bin/bash -u\n",
        "new window": Key("ctrl-n"),
        # "next window": [alt_tab_hold(), time_delay(2), Key("right"), alt_relase()] ,
        # "last window": [alt_tab_hold(), time_delay(2), Key("left"), alt_relase()],
        # 'next app': Key('cmd-tab'),
        # 'last app': Key('cmd-shift-tab'),
        "next tab": Key("ctrl-tab"),
        "(last | preev) tab": Key("ctrl-shift-tab"),
        "new tab": Key("ctrl-t"),
        # "next space": Key("cmd-alt-ctrl-right"),
        # "last space": Key("cmd-alt-ctrl-left"),
        "zoom [in]": Key("ctrl-="),
        "zoom out": Key("ctrl--"),
        "(page | scroll) up": Key("pgup"),
        "(page | scroll) [down]": Key("pgdown"),
        "copy": Key("ctrl-c"),
        "cut": Key("ctrl-x"),
        "paste": Key("ctrl-v"),
        # "menu help": Key("cmd-shift-?"),
        "spotlight": Key(
            "win-s"
        ),  # spotlight search bar in mac corresponding to windows search bar
        "(undo | under | skunks)": Key("ctrl-z"),
        "redo": Key("ctrl-shift-z"),
        "(crap | clear | scratch )": Key("ctrl-backspace"),
        "(select | sell | cell) all": Key("ctrl-a"),
        # "more bright": Key("brightness_up"),
        # "less bright": Key("brightness_down"),
        # "volume up": Key("volume_up"),
        # "volume down": Key("volume_down"),
        # "mute": Key("mute"),
        # "play next": Key("next"),
        # "play previous": Key("previous"),
        # "(play | pause)": Key("space"),  # spotify
        "(wipe | vipe)": Key("backspace"),
        "(pad | padding ) ": ["  ", Key("left")],
        "funny": "haha",
        "arch hive": Key(key_pressify_string("arxiv")),
        # "menubar": Key("ctrl-f2"),
        # "status menu": Key("ctrl-f8"),
        # "my doc": Key("ctrl-f3"),
        "{standard.vocab}": inputs_vocab,
    }
)

ctx.set_list("vocab", vocab)
ctx.keymap(keymap)
