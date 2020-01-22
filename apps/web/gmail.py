import time
from talon.voice import Context, Key, press
from talon import ctrl
from ...utils import time_delay


def helper(app, win):
    # print(win.title.lower().find("gmail - google chrome")>0)
    return win.title.lower().find("gmail - google chrome") > 0


# def normal_mode():
#     # get out of any text box
#     press("escape")
#     # make sure we are in normal mode
#     press("escape")


# def page_mode():
#     normal_mode()
#     # insert ignore mode
#     # press("ctrl-alt-escape")
#     press("i")


# @contextlib.contextmanager
# def page_mode_context():
#     page_mode()
#     yield
#     normal_mode()


def send_string_to_page(string=None):
    def function(m):
        # with page_mode_context():
        # time.sleep(0.3)
        for character in string:
            press(character)
            time.sleep(0.1)

    return function


def send_key_to_page(key=None):
    def function(m):
        # with page_mode_context():
        # time.sleep(0.3)
        # press("ctrl-]")
        press(key)

    return function


ctx = Context("gmail", func=helper)

ctx.keymap(
    {
        "thread (next | neck)": send_string_to_page("j"),
        "thread (previous | preev)": send_string_to_page("k"),
        # Compose and Chat Commands
        # "go inbox": send_string_to_page("gi"),
        "help": send_key_to_page("shift-?"),
        "search mail": send_key_to_page("/"),
        "compose new tab": send_key_to_page("d"),
        "(preev | previous) message": send_key_to_page("p"),
        "next message": send_key_to_page("n"),
        "focus main window": send_key_to_page("shift-escape"),
        "focus latest chat": send_key_to_page("escape"),
        "advance to next chat": send_key_to_page("ctrl-."),
        "advance to previous chat": send_key_to_page("ctrl-,"),
        "send message": send_key_to_page("ctrl-enter"),
        # "send email": send_key_to_page("cmd-enter"),
        "add cc": send_key_to_page("ctrl-shift-c"),
        # "add cc": send_key_to_page("cmd-shift-c"),
        "add bcc": send_key_to_page("ctrl-shift-b"),
        # "add bcc": send_key_to_page("cmd-shift-b"),
        "access custom form": send_key_to_page("ctrl-shift-f"),
        # "access custom form": send_key_to_page("cmd-shift-f"),
        "insert link": send_key_to_page("ctrl-k"),
        # "insert link": send_key_to_page("cmd-k"),
        "go to next misspelled word": send_key_to_page("ctrl-'"),
        "open spelling suggestions": send_key_to_page("ctrl-m"),
        # Formatting Text
        "previous font": send_key_to_page("ctrl-shift-5"),
        "next font": send_key_to_page("ctrl-shift-6"),
        "decrease (text size | font)": send_key_to_page("ctrl-shift--"),
        "increase (text size | font)": send_key_to_page("ctrl-shift-+"),
        "bold": Key("ctrl-b"),
        "italic": Key("ctrl-i"),
        "underline": Key("ctrl-u"),
        "numbered list": Key("ctrl-shift-7"),
        "bulleted list": Key("ctrl-shift-8"),
        "quote": Key("ctrl-shift-9"),
        "indent less": Key("ctrl-["),
        "indent more": Key("ctrl-]"),
        "align left": Key("ctrl-shift-l"),
        "align center": Key("ctrl-shift-e"),
        "align right": Key("ctrl-shift-r"),
        # "remove formatting": Key("ctrl-\\"), #clash with 1password
        # Actions
        "focus toolbar": send_key_to_page(","),
        "select (conversation | message)": send_key_to_page("x"),
        "(toggle star | rotate among superstars)": send_key_to_page("s"),
        "archive": send_key_to_page("e"),
        "mute conversation": send_key_to_page("m"),
        "report spam": send_key_to_page("!"),
        "delete mail": send_key_to_page("#"),
        "undo last": send_key_to_page("z"),
        "reply": send_key_to_page("r"),
        "reply [in] new window": send_key_to_page("shift-r"),
        "reply all": send_key_to_page("a"),
        "replay all in new window": send_key_to_page("shift-a"),
        "forward": send_key_to_page("f"),
        "forward [in] new window": send_key_to_page("shift-f"),
        "update conversation": send_key_to_page("shift-n"),
        "archive conversation and previous": send_key_to_page("]"),
        "archive conversation and next": send_key_to_page("["),
        "mark unread [from selected message]": send_key_to_page("_"),
        # "mark as important": send_key_to_page("+"),
        "mark as important": send_key_to_page("="),
        "mark as not important": send_key_to_page("-"),
        "snooze": send_key_to_page("b"),
        "expand entire conversation": send_key_to_page(";"),
        "collapse entire conversation": send_key_to_page(":"),
        "add conversation to task": send_key_to_page("shift-t"),
        # Hangout
        "show menu": send_string_to_page("hm"),
        "show archived hangouts": send_string_to_page("ha"),
        "show hangout requests": send_string_to_page("hi"),
        "focus conversation list": send_string_to_page("hc"),
        # "open phone": send_string_to_page("g-p"),
        "open phone": send_string_to_page("hp"),
        # Jumping
        "go [to] inbox": send_string_to_page("gi"),
        "go [to] starred [conversations]": send_string_to_page("gs"),
        "go [to] sent [messages]": send_string_to_page("gt"),
        "go [to] drafts": send_string_to_page("gd"),
        "go [to] all mail": send_string_to_page("ga"),
        # "switch to inbox": send_key_to_page("ctrl-alt-,"),
        # "switch to inbox": send_key_to_page("cmd-alt-,"),
        # "switch from inbox": send_key_to_page("ctrl-alt-."),
        # "switch from inbox": send_key_to_page("cmd-alt-."),
        "go to tasks": send_string_to_page("gk"),
        "go to label": send_string_to_page("gl"),
        # Threadlist Selection
        "select all conversation": send_string_to_page("*a"),
        "deselect all [conversation]": send_string_to_page("*n"),
        "select read [conversation]": send_string_to_page("*r"),
        "select unread [conversation]": send_string_to_page("*u"),
        "select starred [conversation]": send_string_to_page("*s"),
        "select unstarred [conversation]": send_string_to_page("*t"),
        # Navigation
        "[back] to threadlist": send_key_to_page("u"),
        "newer [conversation]": send_key_to_page("k"),
        "older [conversation]": send_key_to_page("j"),
        "open [conversation]": send_key_to_page("o"),
        # "open conversation": send_key_to_page("'"),
        "go to next inbox section": send_key_to_page("`"),
        "go to previous inbox section": send_key_to_page("~"),
        # Application
        "compose": send_key_to_page("c"),
        "compose in new tab": send_key_to_page("d"),
        "search mail": send_key_to_page("/"),
        "search chat contacts": send_key_to_page("g"),
        "open more actions": send_key_to_page("."),
        "open move to": send_key_to_page("v"),
        "open label as": send_key_to_page("l"),
        "[open] keyboard [shortcut] help": send_key_to_page("?"),
    }
)
