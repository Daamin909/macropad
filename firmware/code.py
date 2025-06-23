# Daamin's macropad firmware
# Rev 1.1
# Copyright 2024
# Licensed under zlib license
import board
import busio

from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation
from kmk.modules.macros import Macros, Press, Release, Tap
from kmk.modules.encoder import EncoderHandler
from kmk.extensions.media_keys import MediaKeys
from kmk.modules.mouse_keys import MouseKeys


ROTA = board.D6
ROTB = board.D10
COL1 = board.D0
COL2 = board.D1
COL3 = board.D2
COL4 = board.D3
ROW1 = board.D9
ROW2 = board.D8
ROW3 = board.D7


keyboard = KMKKeyboard()

encoder_handler = EncoderHandler()
keyboard.modules.append(MediaKeys())
keyboard.modules.append(MouseKeys())
encoder_handler.pins = ((ROTA, ROTB, None),)
encoder_handler.map = [((KC.VOLU, KC.VOLD),), ]  

macros = Macros()
keyboard.modules.append(macros)
keyboard.modules.append(encoder_handler)


keyboard.col_pins = (COL1, COL2, COL3, COL4)
keyboard.row_pins = (ROW1, ROW2, ROW3)
keyboard.diode_orientation = DiodeOrientation.COL2ROW


OPEN_VSC = KC.MACRO(Press(KC.LGUI), Tap(KC.SPACE), Release(KC.LGUI), "vsc", Tap(KC.ENTER))
OPEN_SPOTIFY = KC.MACRO(Press(KC.LGUI), Tap(KC.SPACE), Release(KC.LGUI), "spotify", Tap(KC.ENTER))
OPEN_BRAVE = KC.MACRO(Press(KC.LGUI), Tap(KC.SPACE), Release(KC.LGUI), "brave", Tap(KC.ENTER))
OPEN_DISCORD = KC.MACRO(Press(KC.LGUI), Tap(KC.SPACE), Release(KC.LGUI), "discord", Tap(KC.ENTER))
MISSION_CTRL = KC.MACRO(
    Press(KC.LALT),
    Press(KC.LSHIFT),
    Tap(KC.M),
    Release(KC.LSHIFT),
    Release(KC.LALT),
)
keyboard.keymap = [
    [KC.MRWD, KC.MFFD, KC.MW_UP, KC.LGUI(KC.V), OPEN_BRAVE, MISSION_CTRL, KC.MW_DN, KC.LGUI(KC.C), OPEN_VSC, OPEN_SPOTIFY, OPEN_DISCORD, KC.MPLY]
]

if __name__ == '__main__':
    keyboard.go()

