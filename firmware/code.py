# Daamin's macropad firmware
# Rev 1.1
# Copyright 2024
# Licensed under zlib license
import board
import busio

from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation
from kmk.modules.macros import Macros


COL1 = board.GP26
COL2 = board.GP27
COL3 = board.GP28
COL4 = board.GP29
ROW1 = board.GP1
ROW2 = board.GP2
ROW3 = board.GP4

keyboard = KMKKeyboard()

macros = Macros()
keyboard.modules.append(macros)

keyboard.col_pins = (COL1, COL2, COL3, COL4)
keyboard.row_pins = (ROW1, ROW2, ROW3)
keyboard.diode_orientation = DiodeOrientation.COL2ROW


keyboard.keymap = [
    [KC.A,      KC.B,   KC.C, KC.D  ],
    [KC.E,      KC.F,     KC.G,      KC.H  ],
    [KC.I,      KC.J,     KC.K,      KC.L  ],
]

if __name__ == '__main__':
    keyboard.go()
