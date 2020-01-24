import os

from talon.voice import Context, Key

from ..utils import key_pressify_string

context = Context("personal")
cwd = os.path.dirname(os.path.realpath(__file__))
text_file = os.path.join(
    cwd, "C:\\Users\\herse\\AppData\\Roaming\\talon\\user\\personal_text.csv"
)

keys = {}
with open(text_file, "r") as f:
    for h in f:
        h = h.rstrip().replace("\\n", "\n")
        h = h.split("=")
        keys[h[0]] = h[1]

context.keymap(keys)
