import time
from talon import ctrl, tap, ui
from talon.voice import Context, Key
import math

ctx = Context("mouse", exe="C:\\WINDOWS\\system32\\mspaint.exe")

def do_fancy_drawing(m):
        x0, y0 = ctrl.mouse_pos()
        n=1000
        amp=50
        for i in range(n):
            t=(float(i)/float(n))*2*math.pi
            x=x0+amp*math.sin(1*t)  + amp*math.sin(3*t) + amp*math.sin(5*t)
            y=y0+amp*math.cos(1*t)  + amp*math.cos(3*t) + amp*math.cos(5*t)
            ctrl.mouse_move(x,y)
            ctrl.mouse_click()
            time.sleep(0.01)

keymap = {
    "draw fancy stuff": do_fancy_drawing
}

ctx.keymap(keymap)
