import curses
import sys
import json
import os
import re

file_name = sys.argv[1]


CONTINUE = "┃"
ITEM = "┣"
END = "┗"

VIEW = 0
EDIT = 1

SHIFT_UP = ord('ő')
SHIFT_DOWN = ord('Ő')
SHIFT_RIGHT = ord('ƒ')

SPECIAL = 'ő'

PRIMARY_COLOR = curses.COLOR_RED

SPECIAL_KEYS = [curses.KEY_UP,curses.KEY_DOWN,curses.KEY_LEFT,curses.KEY_RIGHT]
SPECIAL_CHARS = [SHIFT_DOWN,SHIFT_UP,SHIFT_RIGHT]


