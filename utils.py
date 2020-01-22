from talon.voice import Str, press
import talon.clip as clip
from talon import resource
from .bundle_groups import FILETYPE_SENSITIVE_BUNDLES
import json
import time

# overrides are used as a last resort to override the output. Some uses:
# - frequently misheard words
# - force homophone preference (alternate homophones can be accessed with homophones command)

# To add an override, add the word to override as the key and desired replacement as value in overrides.json
mapping = json.load(resource.open("overrides.json"))

# used for auto-spacing
punctuation = set(".,-!?")


def remove_dragon_junk(word):
    return str(word).lstrip("\\").split("\\", 1)[0]


def parse_word(word):
    word = remove_dragon_junk(word)
    word = mapping.get(word.lower(), word)
    return word


def join_words(words, sep=" "):
    out = ""
    for i, word in enumerate(words):
        if i > 0 and word not in punctuation:
            out += sep
        out += word
    return out


def parse_words(m):
    return list(map(parse_word, m.dgndictation.words))


def insert(s):
    Str(s)(None)


def text(m):
    insert(join_words(parse_words(m)).lower())


def sentence_text(m):
    text = join_words(parse_words(m)).lower()
    insert(text.capitalize())


def word(m):
    text = extract_word(m)
    insert(text.lower())


def extract_word(m):
    return join_words(list(map(parse_word, m.dgnwords.words)))


# FIX ME
def surround(by):
    def func(i, word, last):
        if i == 0:
            word = by + word
        if last:
            word += by
        return word

    return func


# support for parsing numbers as command postfix
def numeral_map():
    numeral_map = dict((str(n), n) for n in range(0, 20))
    for n in [20, 30, 40, 50, 60, 70, 80, 90]:
        numeral_map[str(n)] = n
    numeral_map["oh"] = 0  # synonym for zero
    return numeral_map


def numerals():
    return " (" + " | ".join(sorted(numeral_map().keys())) + ")+"


def optional_numerals():
    return " (" + " | ".join(sorted(numeral_map().keys())) + ")*"


def text_to_number(m):
    tmp = [str(s).lower() for s in m]
    words = [parse_word(word) for word in tmp]

    result = 0
    factor = 1
    for word in reversed(words):
        if word not in optional_numerals():
            # we consumed all the numbers and only the command name is left.
            break

        result = result + factor * int(numeral_map()[word])
        factor = 10 * factor

    return result


number_conversions = {"oh": "0"}  # 'oh' => zero
for i, w in enumerate(
    ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
):
    number_conversions[str(i)] = str(i)
    number_conversions[w] = str(i)
    number_conversions["%s\\number" % (w)] = str(i)


def parse_words_as_integer(words):
    # TODO: Once implemented, use number input value rather than manually
    # parsing number words with this function

    # Ignore any potential non-number words
    number_words = [w for w in words if str(w) in number_conversions]

    # Somehow, no numbers were detected
    if len(number_words) == 0:
        return None

    # Map number words to simple number values
    number_values = list(map(lambda w: number_conversions[w.word], number_words))

    # Filter out initial zero values
    normalized_number_values = []
    non_zero_found = False
    for n in number_values:
        if not non_zero_found and n == "0":
            continue
        non_zero_found = True
        normalized_number_values.append(n)

    # If the entire sequence was zeros, return single zero
    if len(normalized_number_values) == 0:
        normalized_number_values = ["0"]

    # Create merged number string and convert to int
    return int("".join(normalized_number_values))


def is_in_bundles(bundles):
    return lambda app, win: any(b in app.bundle for b in bundles)


def is_filetype(extensions=()):
    def matcher(app, win):
        if is_in_bundles(FILETYPE_SENSITIVE_BUNDLES)(app, win):
            if any(ext in win.title for ext in extensions):
                return True
            else:
                return False
        return True

    return matcher


def preserve_clipboard(fn):
    def wrapped_function(*args, **kwargs):
        old = clip.get()
        ret = fn(*args, **kwargs)
        sleep(0.1)
        clip.set(old)
        return ret

    return wrapped_function


#convert a string into key press format for the talon.voice.Key method
def key_pressify_string(s):
    res = []
    for character in s:
        if character == " ":
            res.append("space ")
        else:
            res.extend([character, " "])

    return "".join(res)

#insert time delay between key presses
def time_delay(n):
    return lambda m: time.sleep(n)

def snake_text(m):
    insert(join_words(parse_words(m), sep="_").lower())

def extract_num_from_m(m, default=ValueError):
    numeral_map = dict((str(n), n) for n in range(0, 10))
    numeral_list = sorted(numeral_map.keys())
    # loop identifies numbers in any message
    number_words = [w for w in m._words if w in numeral_list]
    if len(number_words) == 0:
        if default is ValueError:
            raise ValueError("No number found")
        else:
            return default
    return text_to_number(number_words)

def paste_text(text):
    with clip.revert():
        clip.set(text)
        press("ctrl-v")
        time.sleep(0.1)

@preserve_clipboard
def jump_to_target(target):
    press("cmd-left", wait=2000)
    press("cmd-shift-right", wait=2000)
    press("cmd-c", wait=2000)
    press("left", wait=2000)
    line = clip.get()
    print("LINE")
    print(line)
    result = line.find(target)
    if result == -1:
        return
    for i in range(0, result):
        press("right", wait=0)
    for i in range(0, len(target)):
        press("shift-right")
    press("right", wait=0)