from talon.voice import Context, Key
from ...utils import time_delay
from ...utils import key_pressify_string

context = Context("common_websites", exe="C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe")

keymap = {
    "com dot": ".com",
    "get ( hub | hop )": "github",
    "(lead | leet | elite ) code": Key(key_pressify_string("leetcode")),
    "(over leaf | overleaf | over leave)": Key(key_pressify_string("overleaf"))
}

context.keymap(keymap)
