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



def render_list(t):
	name = t.name
	if t == get_select():
		name = SPECIAL
	N = len(t.children)
	if N!=0:
		name+="┓"
	answer = [name]
	for i in range(N):
		child = t.children[i]
		rendered_child = render_list(child)
		spaces = (len(t.name))*" "
		if i == N-1:
			answer+=augment(spaces+END,spaces+" ",rendered_child)
		else:
			answer+=augment(spaces+ITEM,spaces+CONTINUE,rendered_child)
	return answer

pminrow = 0

def render(pad,data):
	global pminrow
	RENDER_LIST = render_list(data)
	pad.clear()
	rs = get_render_string(data)
	rsl = rs.split(SPECIAL)
	pad.addstr(rsl[0])
	if get_mode() == VIEW:
		pad.addstr(get_select().name,curses.color_pair(1))
	else:
		st = " "
		if len(get_select().name)!=0:
			st = get_select().name
		pad.addstr(st,curses.color_pair(2))
	pad.addstr(rsl[1])
	HEIGHT = curses.LINES
	WIDTH = curses.COLS
	s_id = get_index(get_select())
	if s_id < pminrow:
		pminrow = s_id
	if s_id - pminrow >= HEIGHT:
		pminrow = s_id - HEIGHT +1
	pad.refresh(pminrow,0,0,0,HEIGHT-1,WIDTH-1)

def get_render_string(data):
	RENDER_LIST = render_list(data)
	s = ""
	for i in range(len(RENDER_LIST)):
		s+=RENDER_LIST[i]
		s+="\n"
	return s