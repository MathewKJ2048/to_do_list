from conf import *
from task import *
from render import *
from control import *

def process_edit(key):
	select = get_select()
	if key in SPECIAL_KEYS or ord(chr(key)) in SPECIAL_CHARS:
		return
	if key == curses.KEY_BACKSPACE:
		if len(select.name)==0 and len(select.children)==0:
			purge()
			view_mode()
			return
		select.name = select.name[:-1]
		return
	select.name+=chr(key)

def process(key):
	if key != -1:
		if get_mode() == VIEW:
			if key == ord('q'):
				clean_quit()
			elif key == curses.KEY_UP:
				sibling(-1)
			elif key == curses.KEY_DOWN:
				sibling(1)
			elif key == curses.KEY_LEFT:
				parent()
			elif key == curses.KEY_RIGHT:
				child()
			elif key == SHIFT_RIGHT:
				if create_child():
					edit_mode()
			elif key == SHIFT_UP:
				if create_sibling():
					edit_mode()
			elif key == SHIFT_DOWN:
				if create_sibling(successor=True):
					edit_mode()
			elif key == curses.KEY_ENTER or key == ord('\n') or key == ord("\r"):
				edit_mode()
			elif key == curses.KEY_DC:
				toggle_complete()
		elif get_mode() == EDIT:
			if key == curses.KEY_ENTER or key == ord('\n') or key == ord("\r"):
				view_mode()
			else:
				process_edit(key)

def main(stdscr):

	curses.use_default_colors()
	curses.init_pair(1,PRIMARY_COLOR, -1) # VIEW mode
	curses.init_pair(2,-1,PRIMARY_COLOR) # EDIT mode
	curses.curs_set(0)
	stdscr.clear()
	stdscr.refresh()
	pad = curses.newpad(1024,1024)

	assert get_select()!=None

	

	while True:
		render(pad,data)
		key = stdscr.getch()
		process(key)
		if key == ord('q')and get_mode() == VIEW:
			break
		

def outro():
	print("panic exit: save changes? y/n")
	ch = input()
	if ch == 'Y' or ch == 'y':
		clean_quit()

try:
	curses.wrapper(main)
except Exception as e:
	print(e)
	outro()
except KeyboardInterrupt:
	outro()

	