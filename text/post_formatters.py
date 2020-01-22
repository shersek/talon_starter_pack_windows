from talon.voice import Context, Key, press, Str
from ..utils import time_delay, surround
from talon import ui, clip

context = Context("post_formatting")

formatters = {
    "dunder": (True, lambda i, word, _: "__%s__" % word if i == 0 else word),
    "camel": (True, lambda i, word, _: word if i == 0 else word.capitalize()),
    "snake": (True, lambda i, word, _: word.lower() if i == 0 else "_" + word.lower()),
    "smash": (True, lambda i, word, _: word),
    "kebab": (True, lambda i, word, _: word if i == 0 else "-" + word),
    "pack": (True, lambda i, word, _: word if i == 0 else "::" + word),
    "title": (False, lambda i, word, _: word.capitalize()),
    "allcaps": (False, lambda i, word, _: word.upper()),
    "alldown": (False, lambda i, word, _: word.lower()),
    "dubstring": (False, surround('"')),
    "string": (False, surround("'")),
    "padded": (False, surround(" ")),
    "dotted": (True, lambda i, word, _: word if i == 0 else "." + word),
    "slasher": (True, lambda i, word, _: "/" + word),
    "slayer": (True, lambda i, word, _: "\\" + word),
}


def PostFormatText(m):
    prev_clip = clip.get()
    press("ctrl-c")
    fmt = []
    for w in m._words[1:]:
        if w in formatters:
            fmt.append(w)
        else:
            break
    words= clip.get().split()
    tmp = []
    spaces = True
    for i, w in enumerate(words):
        for name in reversed(fmt):
            smash, func = formatters[name]
            w = func(i, w, i == len(words) - 1)
            spaces = spaces and not smash
        tmp.append(w)
    words = tmp

    sep = " "
    if not spaces:
        sep = ""
    clip.set(prev_clip)
    Str(sep.join(words))(None)

keymap ={

    "post (%s)" % (" | ".join(formatters)): PostFormatText,

}

context.keymap(keymap)
