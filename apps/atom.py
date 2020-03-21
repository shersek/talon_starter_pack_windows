import os
import re
import time

from talon import ui
from talon.voice import Context, Key, Rule, Str, press

from .. import utils

from ..utils import (  # numeral_map,; numerals,; optional_numerals,; remove_dragon_junk,
    extract_num_from_m,
    parse_words_as_integer,
    text,
    insert,
)

# atom has two executables, for versions 1.42.0 and 1.43.0
# ctx = Context(
#     "atom", exe="C:\\Users\\herse\\AppData\\Local\\atom\\app-1.42.0\\atom.exe"
# )

ctx = Context("atom", func=lambda apps, win: apps.name == "atom.exe")


atom_hotkey = "shift-ctrl-alt-t"
atom_command_pallet = "ctrl-shift-p"


class Struct:
    def __init__(self, **entries):
        self.__dict__.update(entries)


COMMANDS = Struct(
    DELETE_TO_BOL="b",
    DELETE_TO_EOL="e",
    SELECT_LINES="s",
    FIND_NEXT="f",
    FIND_PREVIOUS="p",
    COPY_LINE="c",
    MOVE_LINE="m",
    SELECT_UNTIL="u",
)


def execute_atom_command(command, parameters=None):
    press(atom_hotkey)
    press(command)
    if parameters:
        Str(parameters)(None)
        press("enter")


def find_next(m):
    text = "".join(utils.parse_words(m)).lower()
    if text:
        execute_atom_command(COMMANDS.FIND_NEXT, text)


def find_previous(m):
    text = "".join(utils.parse_words(m)).lower()
    if text:
        execute_atom_command(COMMANDS.FIND_PREVIOUS, text)


def select_lines(m):
    # NB: line_range is e.g. 99102, which is parsed in
    #  the atom package as lines 99..102
    line_range = extract_num_from_m(m)
    execute_atom_command(COMMANDS.SELECT_LINES, str(line_range))


def select_till(m):
    line_range = extract_num_from_m(m)
    execute_atom_command(COMMANDS.SELECT_UNTIL, str(line_range))


def change_pain(m=None, line=None):
    if line is None:
        line = extract_num_from_m(m)

    for i in range(10):
        press("ctrl-k")
        press("ctrl-left")
    for i in range(1, line):
        press("ctrl-k")
        press("ctrl-right")


def jump_tab(m, tab_number=None):
    if tab_number is None:
        tab_number = parse_words_as_integer(m._words[1:])
    print(tab_number)
    if tab_number is not None and tab_number > 0:
        if tab_number < 10:
            press("alt-%s" % tab_number)
        else:
            change_pain(line=int(tab_number / 10))
            press("alt-%s" % (tab_number % 10))


def command_from_palette(command):
    press(atom_command_pallet)
    time.sleep(0.2)
    utils.paste_text(command)
    time.sleep(0.1)
    press("enter")


def command(command):
    def function(m):
        command_from_palette(command)

    return function


snippets = {
    "import": "im",
    "from": "fim",
    "class": "class",
    "method": "defs",
    "function": "def",
    "property": "property",
    "condition": "if",
    "for loop": "for",
    "while loop": "while",
    "list comp": "lc",
    "list condition": "lcie",
    "dictionary": "dc",
    "set": "sc",
    "if main": "ifmain",
}


def code_snippet(m):
    snippet_key = m["atom.snippets"]
    utils.insert(snippets[snippet_key])
    time.sleep(0.5)
    press("tab")


keymap = {
    "(show | view) sets": Key("ctrl-,"),
    "search for": Key("ctrl-f"),
    "crew <dgndictation>": find_next,
    "trail <dgndictation>": find_previous,
    "shackle": Key("ctrl-l"),
    "selrang " + utils.numerals() + " [over]": select_lines,
    "(seltill | sell till | cell tell)" + utils.numerals() + " [over]": select_till,
    "peach": Key("ctrl-t"),
    "peach <dgndictation>": [Key("ctrl-t"), text],
    "(pain | bang)" + utils.numerals(): change_pain,
    "tabby" + utils.numerals(): jump_tab,
    "lefty tab": Key("shift-ctrl-tab"),
    "righty tab": Key("ctrl-tab"),
    "split pain left": [Key("ctrl-k"), Key("left")],
    "split pain right": [Key("ctrl-k"), Key("right")],
    "split pain up": [Key("ctrl-k"), Key("up")],
    "split pain down": [Key("ctrl-k"), Key("down")],
    "go pain left": [Key("ctrl-k"), Key("ctrl-left")],
    "go pain right": [Key("ctrl-k"), Key("ctrl-right")],
    "go pain up": [Key("ctrl-k"), Key("ctrl-up")],
    "go pain down": [Key("ctrl-k"), Key("ctrl-down")],
    "close pain": [Key("ctrl-k"), Key("ctrl-w")],
    "restore [tab]": command("pane reopen"),
    "command pallet": Key(atom_command_pallet),
    "((cursor | curr) (center | mid) | curse enter)": command(
        "center-line:toggle"
    ),  # need center-line atom package
    "(cursor | curr) top": [
        command("center-line:toggle"),
        command("center-line:toggle"),
    ],
    "(select | cell) [inside] (quote | quotes | string)": command(  # need to expand selection atom package
        "expand-selection-to-quotes:toggle"
    ),
    # needs bracket-matcher atom package; still a bit poor.
    "(bracken | select inside brackets)": command(
        "bracket-matcher:select-inside-bracket"
    ),
    "go match": command("bracket-matcher:go-to-matching-bracket"),
    "remove [matching] (bracket | brackets)": command(
        "bracket-matcher:remove-matching-brackets"
    ),
    # # python
    "quinn if": ["if :", Key("left")],
    "quinn to do": "# TODO: ",
    "(quinn | queen | cringe) {atom.snippets}": code_snippet,
    # TODO:
    # github
    # "jet hub open": command("open-on-github:file"),
    # "jet hub copy": command("open-on-github:copy-url"),
    # "jet hub blame": command("open-on-github:blame"),
    # "jet hub repository": command("open-on-github:repository"),
    # "jet hub history": command("open-on-github:history"),
    # "jet hub issues": command("open-on-github:issues"),
    # "jet hub pull requests": command("open-on-github:pull-requests"),
    # "jet hub branch compare": command("open-on-github:branch-compare"),
    # autocomplete-python
    "(go to | spring) (definition | def)": command(
        "autocomplete-python:go-to-definition"
    ),
    "show (usages | usage)": command("autocomplete-python:show-usages"),
    "complete arguments": command("autocomplete-python:complete-arguments"),
    "python rename": command("autocomplete-python:rename"),
    "override method": command("autocomplete-python:override-method"),
    # symbols-view
    "(go to | spring) (symbol | sim)": command("symbols-view:toggle-file-symbols"),
    "(go to | spring) (symbol | sim) <dgndictation> [over]": [
        command("symbols-view:toggle-file-symbols"),
        lambda m: time.sleep(0.5),
        text,
        Key("enter"),
        command("center-line:toggle"),
    ],
    # folding
    "fold all": command("editor:fold-all"),
    "unfold all": command("editor:unfold-all"),
    "fold [current row]": command("editor:fold-current-row"),
    "unfold [current row]": command("editor:unfold-current-row"),
    # project
    "add project [folder]": command("application:add-project-folder"),
    "remove project [folder]": command("tree view remove"),
    # cursor-history
    "(cursor | curr) (previous | preev | back)": command("cursor history prev"),
    "(cursor | curr) next": command("cursor history next"),
    # config
    "edit snippets": command("application open snippets"),
    "edit key map": command("application open keymap"),
    "install packages": command("settings view install packages and themes"),
    # linter
    "lint (next | neck)": command("linter ui default: next in current file"),
    "lint (preev | previous)": command("linter ui default: previous in current file"),
    # atom-isort
    "sort imports": command("atom isort sort imports"),
    # atom-blacken
    "(atom | adam) black": command("atom blacken"),
    # platformio-ide-terminal
    "(platform | terminal | termy | termie) new": command("platformio new"),
    "(platform | terminal | termy | termie) (toggle | switch)": command(
        "platformio toggle"
    ),
    "(platform | terminal | termy | termie) (previous | preev)": command(
        "platformio prev"
    ),
    "(platform | terminal | termy | termie) next": command("platformio next"),
    "(platform | terminal | termy | termie) (cell | sell)": command(
        "platformio insert selected"
    ),
    "(platform | terminal | termy | termie) close": command("platformio close"),
    "(platform | terminal | termy | termie) close all": command("platformio close all"),
    # atom-script
    "(code | script) (run | sprint | go)": command("script run"),
    "script close": command("script close view"),
    "(code | script) kill": Key("ctrl-q"),
    "(rep | rap | wrap) (toggle | switch)": command("toggle soft wrap"),
    # bookmark
    "(bookmark | mark) toggle": command("bookmark toggle"),
}
ctx.set_list("snippets", snippets.keys())
ctx.keymap(keymap)
