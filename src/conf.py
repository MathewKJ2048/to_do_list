import curses
import sys
import json
import os
import re

file_name = sys.argv[1]

# these are associated with the control codes
SHIFT_UP = ord('ő')    # create older sibling node
SHIFT_DOWN = ord('Ő')  # create younger sibling node
SHIFT_RIGHT = ord('ƒ') # create child

# 8 variants exist. Finer control can be exercised by editing the curses.init_pair() in main() in main.py
PRIMARY_COLOR = curses.COLOR_RED

SPECIAL_KEYS = [curses.KEY_UP,curses.KEY_DOWN,curses.KEY_LEFT,curses.KEY_RIGHT]
SPECIAL_CHARS = [SHIFT_DOWN,SHIFT_UP,SHIFT_RIGHT]

# number of spaces to use when saving json file
INDENT_NUMBER = 4

# enums
VIEW = 0
EDIT = 1

# can be any character which will never be used normally
SPECIAL = 'ő'


