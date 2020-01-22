from talon.voice import Context, Key

context = Context("1password")

context.keymap(
    {
        # Global
        "password fill": Key("ctrl-\\"),
        "password show": Key("alt-ctrl-\\"),

        # App
        "open one password": Key("ctrl-shift-\\"),
        "password new": Key("ctrl-n"),
        "password dup": Key("ctrl-d"),
        "(password edit | password make edits)": Key("ctrl-e"),
        "password delete": Key("ctrl-delete"),
    }
)
