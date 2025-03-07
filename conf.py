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


