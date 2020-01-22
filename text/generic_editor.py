from talon.voice import Key, press, Str, Context
from ..utils import (
    parse_word,
    numerals,
    optional_numerals,
    text_to_number,
    jump_to_target,
)

ctx = Context("generic_editor")

# actions and helper functions
def jump_to_bol(m):
    line = text_to_number(m)
    press("ctrl-g")
    Str(str(line))(None)
    press("enter")


# def jump_to_end_of_line():
#     press("ctrl-right")


# def jump_to_beginning_of_text():
#     press("ctrl-right")

# def jump_to_nearly_end_of_line():
#     press("left")


def jump_to_bol_and(then):
    def fn(m):
        if len(m._words) > 1:
            jump_to_bol(m)
        else:
            press("home")
        then()

    return fn


def jump_to_eol_and(then):
    def fn(m):
        if len(m._words) > 1:
            jump_to_bol(m)
        press("end")
        then()

    return fn


def toggle_comments(*unneeded):
    press("ctrl-/")


def snipline():
    press("shift-end")
    press("delete")


# def get_first_word(m):
#     return m.dgndictation.words[0]
#
# def jump_to(m):
#     target = get_first_word(m)
#     jump_to_target(target)

# for vocabulary guide go to: https://quizlet.com/249263351/voice-code-cards-flash-cards/

keymap = {
    "(trundle | comment) [line]": toggle_comments,
    "(trundle | comment) [line]"
    + numerals(): jump_to_bol_and(toggle_comments),  # noop for plain/text
    "snipline"
    + optional_numerals(): jump_to_bol_and(
        snipline
    ),  # with no arguments will delete entire line. with a single argument will move to that line and delete it.
    "sprinkle"
    + optional_numerals(): jump_to_bol_and(
        lambda: press("home")
    ),  # go to line number then position cursor at beginning of line
    "spring"
    + optional_numerals(): jump_to_bol,  # go to line number to begining of text
    "sprinkoon"
    + numerals(): jump_to_eol_and(
        lambda: press("enter")
    ),  # go to line number then insert a new line below
    "dear" + optional_numerals(): jump_to_eol_and(lambda: None),
    "smear" + optional_numerals(): jump_to_eol_and(lambda: press("left")),
    # file
    "(save | safe) [file]": Key("ctrl-s"),
    "close (file | tab)": Key("ctrl-f4"),
    "new file": Key("ctrl-n"),
    # left, right, up and down already defined
    "go word left": Key("ctrl-left"),
    "go word right": Key("ctrl-right"),
    "go par down": Key("ctrl-down"),
    "go par up": Key("ctrl-up"),
    "go [to] top": Key("ctrl-home"),
    "go [to] bottom": Key("ctrl-end"),
    # selecting
    "(select | sell | cell) left": Key("shift-left"),
    "(select | sell | cell) right": Key("shift-right"),
    "(select | sell | cell) up": Key("shift-up"),
    "(select | sell | cell) down": Key("shift-down"),
    "(select | sell | cell) (word left | stone)": Key("shift-ctrl-left"),
    "(select | sell | cell) (word right | step)": Key("shift-ctrl-right"),
    "(select | sell | cell) (home | pop)": Key("shift-home"),
    "(select | sell | cell) (end | push)": Key("shift-end"),
    "(select | sell | cell) line": [Key("home"), Key("shift-end")],
    "(select | sell | cell) page up": Key("shift-pageup"),
    "(select | sell | cell) page down": Key("shift-pagedown"),
    # deleting
    "(clear | scrap | scratch) (word left | stone)": Key("ctrl-backspace"),
    "(clear | scrap | scratch) (word right | step)": Key("ctrl-delete"),
    "(clear | scrap | scratch) line": [
        Key("end"),
        Key("shift-home"),
        Key("backspace"),
        Key("backspace"),
    ],
    "(clear | scrap | scratch) (home | pop)": [Key("shift-home"), Key("delete")],
    "(clear | scrap | scratch) (end | push)": [Key("shift-end"), Key("delete")],
    # copying
    "copy (word left | stone)": [
        Key("ctrl-shift-left"),
        Key("ctrl-c"),
        Key("ctrl-shift-right"),
    ],
    "copy (word right | step)": [
        Key("ctrl-shift-right"),
        Key("ctrl-c"),
        Key("ctrl-shift-left"),
    ],
    "copy line": [Key("end"), Key("shift-home"), Key("ctrl-c"), Key("end")],
    "copy (home | pop)": [Key("shift-home"), Key("ctrl-c"), Key("right")],
    "copy (end | push)": [Key("shift-end"), Key("ctrl-c"), Key("left")],
    # cutting
    "cut (word left | stone)": [Key("ctrl-shift-left"), Key("ctrl-x")],
    "cut (word right | step)": [Key("ctrl-shift-right"), Key("ctrl-x")],
    "cut line": [Key("end"), Key("shift-home"), Key("ctrl-x")],
    "cut (home | pop)": [Key("shift-home"), Key("ctrl-x")],
    "cut (end | push)": [Key("shift-end"), Key("ctrl-x")],
    # misc
    "indent": Key("tab"),
    "de-dent": Key("shift-tab"),
    "jolt": [Key("ctrl-x"), Key("ctrl-v"), Key("ctrl-v")],
    "(duplicate line | jolt line)": [
        Key("end"),
        Key("shift-home"),
        Key("ctrl-c"),
        Key("end"),
        Key("enter"),
        Key("ctrl-v"),
    ],
    # edit
    # "paste match": Key("cmd-shift-v"),
    # "shove": Key("cmd-]"),
    # "tug": Key("cmd-["),
    # "(scrap | scratch | delete) word": Key("alt-backspace"),
    # "(scrap | scratch | delete) (begin | start)": Key("cmd-backspace"),
    # navigation
    "push": Key("end"),
    "pop": Key("home"),
    "step": Key("ctrl-right"),
    "stone": Key("ctrl-left"),
    # "jump to <dgndictation>": jump_to,
}
ctx.keymap(keymap)
