from conf import *
from task import *
from control import *

def augment(head,tail,rlist):
	if len(rlist)==0:
		return []
	rlist_new = [head+rlist[0]]
	for r in rlist[1:]:
		rlist_new.append(tail+r)
	return rlist_new

def selection_render(s):
	if get_mode() == VIEW:
		return '<'+s+'>'
	else:
		return '['+s+']'

def render_list(t):
	name = t.name
	if t == get_select():
		name = selection_render(name)
	N = len(t.children)
	if N!=0:
		name+="┓"
	answer = [name]
	for i in range(N):
		child = t.children[i]
		rendered_child = render_list(child)
		spaces = (len(name)-1)*" "
		if i == N-1:
			answer+=augment(spaces+END,spaces+" ",rendered_child)
		else:
			answer+=augment(spaces+ITEM,spaces+CONTINUE,rendered_child)
	return answer

def render(pad,data):
	RENDER_LIST = render_list(data)
	pad.clear()
	pad.addstr(get_render_string(data))
	HEIGHT = curses.LINES
	WIDTH = curses.COLS
	pad.refresh(0,0,0,0,HEIGHT-1,WIDTH-1)

def get_render_string(data):
	RENDER_LIST = render_list(data)
	s = ""
	for i in range(len(RENDER_LIST)):
		s+=RENDER_LIST[i]
		s+="\n"
	return s