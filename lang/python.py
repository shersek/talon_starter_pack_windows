from talon.voice import Context, Key
from ..utils import key_pressify_string, snake_text

context = Context("python")

context.keymap(
    {
        "empty dict": "{}",
        "word (dickt | dictionary)": "dict",
        "state (def | deaf | deft)": "def ",
        "state else if": "elif ",
        "state if": "if ",
        "state while args": ["while ()", Key("left")],
        "state while": ["while "],
        "state for": "for ",
        "state for eye in range": ["for i in range()", Key("left")],
        "state switch": ["switch ()", Key("left")],
        "state case": ["case \nbreak;", Key("up")],
        "state goto": "goto ",
        "state import": "import ",
        "state class": "class ",
        "state include": "#include ",
        "state include system": ["#include <>", Key("left")],
        "state include local": ['#include ""', Key("left")],
        "state type deaf": "typedef ",
        "state type deaf struct": ["typedef struct {\n\n};", Key("up"), "\t"],
        "comment py": "# ",
        "dunder in it": "__init__",
        "self taught": "self.",
        "from import": ["from import ", Key("alt-left"), Key("space"), Key("left")],
        "for in": ["for in ", Key("alt-left"), Key("space"), Key("left")],
        # my additions
        "array [index]": ["[]", Key("left")],
        "in range": [Key(key_pressify_string(" in range()")), Key("left")],
        "[list] len": ["len", "()", Key("left")],
        "state (many | mini)": ["min", "()", Key("left")],
        "state (max | maxie)": ["max", "()", Key("left")],
        "popsicle": "pop",
        "(the | dee) queue": "dequeue",
        "heap queue": "heapq",
        "[smash] heap push": "heappush",
        "[smash] heap pop": "heappop",
        # from talon community
        "self assign <dgndictation> [over]": [
            "self.",
            snake_text,
            " = ",
            snake_text,
            "\n",
        ],
        "self": "self",
        "self dot": "self.",
        "self [(dot | doubt)] <dgndictation> [over]": ["self.", snake_text],
        # packages
        "conda": "conda",
        "numpy": "numpy",
        "scipy": "scipy",
        "(tensorflow | tensor flow)": "tensorflow",
        "pandas": "pandas",
        "ex gee boost": "xgboost",
        "python": "python",
        "python 3": "python3",
    }
)
