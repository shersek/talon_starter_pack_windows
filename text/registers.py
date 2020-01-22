from talon.voice import Context, Key, press, Str
from ..utils import time_delay
from talon import ui, clip

context = Context("registers")

regs = {str(i): i for i in range(10)}

global regs_list
regs_list = [str(i) for i in range(10)]


def send_clip_to_register(m):
    press("ctrl-c")
    cur_reg = int(m._words[-1])
    regs_list[cur_reg] = clip.get()
    # print(regs_list)


def paste_from_register(m):
    cur_reg = int(m._words[-1])
    reg_contents = regs_list[cur_reg]
    print(reg_contents)
    Str(reg_contents)(None)


keymap = {
    "(copy | send) (register | reggie) {registers.regs}": send_clip_to_register,
    "(paste  | stick) (register | reggie) {registers.regs}": paste_from_register,
}

context.set_list("regs", regs.keys())
context.keymap(keymap)
