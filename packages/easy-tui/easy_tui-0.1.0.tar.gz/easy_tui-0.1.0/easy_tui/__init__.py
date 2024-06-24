import simple_screen as ssc
from simple_screen.keys import *
LAST_ROW = ssc.DIMENSIONS.h - 1
LAST_COL = ssc.DIMENSIONS.w - 1


widgets = []
tabulatables = []
ix_tab = None
buttons = []

def change_tab(salto):
    global ix_tab
    tabulatables[ix_tab].focus_out()
    ix_tab = (ix_tab + salto) % len(tabulatables)
    tabulatables[ix_tab].focus_in()

def draw():
    ssc.cls()
    for control in widgets:
        control.draw()

@ssc.app
def loop():
    global ix_tab
    if tabulatables:
        tabulatables[0].focus_in()
        ix_tab = 0

    app_on = True
    while app_on:
        key = ssc.inkey()
        if key == ssc.ESC:
            app_on = False
        elif key in (ssc.TAB, ssc.ENTER):
            change_tab(1)
        elif key == ssc.STAB:
            change_tab(-1)

        for control in tabulatables:
            if control.focused:
                control.handle_input(key)

        for control in buttons:
            if control.key == key:
                control.click()

        draw()



    