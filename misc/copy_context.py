from talon.voice import Context, Key
from talon import clip, ui

context = Context("copy_context")

keymap ={
    "copy donkey": lambda m: clip.set(ui.active_app().exe),
}
context.keymap(keymap)


