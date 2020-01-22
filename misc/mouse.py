import time

from talon import ctrl, tap, ui
from talon.voice import Context, Key

# increase to enable smooth scrolling
SCROLL_TOTAL_TIME = 0.0

ctx = Context("mouse")

x, y = ctrl.mouse_pos()
mouse_history = [(x, y, time.time())]
force_move = None


def on_move(typ, e):
    print(e)
    mouse_history.append((e.x, e.y, time.time()))
    if force_move:
        e.x, e.y = force_move
        return True


tap.register(tap.MMOVE, on_move)


def click_pos(m):
    word = m._words[0]
    start = (word.start + min((word.end - word.start) / 2, 0.100)) / 1000.0
    diff, pos = min([(abs(start - pos[2]), pos) for pos in mouse_history])
    return pos[:2]


def click(m, button=0, times=1):
    for _ in range(times):
        ctrl.mouse_click(pos=(x, y), button=button, times=times, wait=16000)


def right_click(m):
    click(m, button=1)


def dubclick(m):
    click(m, button=0, times=2)


def tripclick(m):
    click(m, button=0, times=3)


def press_key_and_click(m, key, button=0, times=1):
    ctrl.key_press(key, down=True)
    ctrl.mouse_click(pos=(x, y), button=button, times=times, wait=16000)
    ctrl.key_press(key, up=True)


def mouse_scroll(amount):
    def scroll(m):
        ctrl.mouse_scroll(y=amount)

    return scroll


def mouse_smooth_scroll(amount):
    def scroll(m):
        if SCROLL_TOTAL_TIME != 0:
            interval = 0.007
            depth = int(SCROLL_TOTAL_TIME // interval)
            split = amount / depth
            for x in range(depth):
                ctrl.mouse_scroll(y=split)
                time.sleep(interval)
        else:
            ctrl.mouse_scroll(y=amount)

    return scroll


def mouse_drag(m):
    x, y = click_pos(m)
    ctrl.mouse_click(pos=(x, y), down=True)


def mouse_release(m):
    x, y = click_pos(m)
    ctrl.mouse_click(pos=(x, y), up=True)


def mouse_center(m):
    win = ui.active_window()
    rect = win.rect
    center = (rect.x + rect.width / 2, rect.y + rect.height / 2)
    print(rect, center)
    ctrl.mouse_move(*center)


def mouse_place(multiplier_string):
    if multiplier_string == "half":
        multiplier = 1
    elif multiplier_string == "full":
        multiplier = 1.8

    def internal(m):
        win = ui.active_window()
        rect = win.rect
        center_x = rect.x + rect.width / 2
        center_y = rect.y + rect.height / 2
        region = regions[m._words[1]]
        if region == "west":
            pos = (center_x - multiplier * rect.width / 4, center_y)
        elif region == "east":
            pos = (center_x + multiplier * rect.width / 4, center_y)
        elif region == "north":
            pos = (center_x, center_y - multiplier * rect.height / 4)
        elif region == "south":
            pos = (center_x, center_y + multiplier * rect.height / 4)
        elif region == "northeast":
            pos = (
                center_x + multiplier * rect.width / 4,
                center_y - multiplier * rect.height / 4,
            )
        elif region == "northwest":
            pos = (
                center_x - multiplier * rect.width / 4,
                center_y - multiplier * rect.height / 4,
            )
        elif region == "southeast":
            pos = (
                center_x + multiplier * rect.width / 4,
                center_y + multiplier * rect.height / 4,
            )
        elif region == "southwest":
            pos = (
                center_x - multiplier * rect.width / 4,
                center_y + multiplier * rect.height / 4,
            )
        ctrl.mouse_move(*pos)

    return internal


def mouse_move_pixels(no_pixels_string):
    if no_pixels_string == "one" or no_pixels_string == "1":
        no_pixels_int = 1
    elif no_pixels_string == "ten":
        no_pixels_int = 10
    if no_pixels_string == "hundred":
        no_pixels_int = 100

    def internal(m):
        cur_x, cur_y = ctrl.mouse_pos()
        region = regions[m._words[1]]
        if region == "west":
            pos = (cur_x - no_pixels_int, cur_y)
        elif region == "east":
            pos = (cur_x + no_pixels_int, cur_y)
        elif region == "north":
            pos = (cur_x, cur_y - no_pixels_int)
        elif region == "south":
            pos = (cur_x, cur_y + no_pixels_int)
        elif region == "northeast":
            pos = (cur_x + no_pixels_int, cur_y - no_pixels_int)
        elif region == "northwest":
            pos = (cur_x - no_pixels_int, cur_y - no_pixels_int)
        elif region == "southeast":
            pos = (cur_x + no_pixels_int, cur_y + no_pixels_int)
        elif region == "southwest":
            pos = (cur_x - no_pixels_int, cur_y + no_pixels_int)
        ctrl.mouse_move(*pos)

    return internal


def shift_click(m, button=0, times=1):
    press_key_and_click(m, "shift", button, times)


def control_click(m, button=0, times=1):
    press_key_and_click(m, "ctrl", button, times)


def command_click(m, button=0, times=1):
    press_key_and_click(m, "cmd", button, times)


def control_shift_click(m, button=0, times=1):
    ctrl.key_press("shift", ctrl=True, shift=True, down=True)
    ctrl.mouse_click(pos=(x, y), button=button, times=times, wait=16000)
    ctrl.key_press("shift", ctrl=True, shift=True, up=True)


regions = {
    "north": "north",
    "south": "south",
    "east": "east",
    "west": "west",
    "northeast": "northeast",
    "northwest": "northwest",
    "southeast": "southeast",
    "southwest": "southwest",
}

keymap = {
    # jsc modified with some voice-code compatibility
    "righty (click | chirff)": right_click,
    "righty press": Key("shift-f10"),
    "(click | chiff)": click,
    "(dubclick | duke)": dubclick,
    "(tripclick | triplick)": tripclick,
    "drag": mouse_drag,
    "drag release": mouse_release,
    "control click": control_click,
    "shift click": shift_click,
    # "(command click | chom lick)": command_click,
    "(control shift click | troll shift click)": control_shift_click,
    "(control shift double click | troll shift double click)": lambda m: control_shift_click(
        m, 0, 2
    ),
    "do park": [dubclick, Key("ctrl-v")],
    "do koosh": [dubclick, Key("ctrl-c")],
    # "wheel down": mouse_smooth_scroll(250),
    # "wheel up": mouse_smooth_scroll(-250),
    # "wheel down here": [mouse_center, mouse_smooth_scroll(250)],
    # "wheel up here": [mouse_center, mouse_smooth_scroll(-250)],
    "mouse center": mouse_center,
    "mouse {mouse.regions} half": mouse_place("half"),
    "mouse {mouse.regions} [full]": mouse_place("full"),
    "move {mouse.regions} (one | 1)": mouse_move_pixels("one"),
    "move {mouse.regions} ten": mouse_move_pixels("ten"),
    "move {mouse.regions} hundred": mouse_move_pixels("hundred"),
}
ctx.set_list("regions", regions.keys())
ctx.keymap(keymap)
