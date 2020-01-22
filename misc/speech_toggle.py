from talon.voice import Context, ContextGroup
from talon.engine import engine
from talon_plugins import speech

sleep_group = ContextGroup("sleepy")
sleepy = Context("sleepy", group=sleep_group)

sleepy.keymap(
    {
        "talon sleep": lambda m: speech.set_enabled(False),
        "talon wake": lambda m: speech.set_enabled(True),
        "dragon mode": [
            lambda m: speech.set_enabled(False),
            lambda m: engine.mimic("switch to normal mode".split()),

        ],
        "talon mode": [
            lambda m: speech.set_enabled(True),
            lambda m: engine.mimic("switch to command mode".split()),
        ],
    }
)
sleep_group.load()
