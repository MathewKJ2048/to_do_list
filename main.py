from conf import *
from task import *
from render import *
from control import *

def process_edit(key):
	select = get_select()
	if key in [curses.KEY_UP,curses.KEY_DOWN,curses.KEY_LEFT,curses.KEY_RIGHT]:
		return
	if key == curses.KEY_BACKSPACE:
		if len(select.name)==0:
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
		elif get_mode() == EDIT:
			if key == curses.KEY_ENTER or key == ord('\n') or key == ord("\r"):
				view_mode()
			else:
				process_edit(key)

def main(stdscr):

	curses.use_default_colors()
	curses.init_pair(1,PRIMARY_COLOR, -1)
	curses.init_pair(2,-1,PRIMARY_COLOR)
	curses.curs_set(0)
	stdscr.clear()
	pad = curses.newpad(1024,1024)

	while True:
		render_aux(pad,data)
		key = stdscr.getch()
		process(key)
		if key == ord('q'):
			break
		
curses.wrapper(main)

	