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

def render_aux(pad, data):
	pad.clear()
	rs = get_render_string(data)
	if SPECIAL in rs:
		rsl = re.split(SPECIAL+"+",rs)
		pad.addstr(rsl[0])
		if get_mode() == VIEW:
			pad.addstr(get_select().name,curses.color_pair(1))
		else:
			st = " "
			if len(get_select().name)!=0:
				st = get_select().name
			pad.addstr(st,curses.color_pair(2))
		pad.addstr(rsl[1])
	else:
		pad.addstr(rs)
	HEIGHT = curses.LINES
	WIDTH = curses.COLS
	pad.refresh(0,0,0,0,HEIGHT-1,WIDTH-1)

def get_render_string(data):
	RENDER_LIST = render_list_aux(data)
	s = ""
	for i in range(len(RENDER_LIST)):
		s+=RENDER_LIST[i]
		s+="\n"
	return s

def col(lc,id,initial=False):
	if lc == []:
		return []
	l = []
	m = 0
	for c in lc:
		e = c.name
		if c == get_select():
			e = len(e)*SPECIAL
		l.append(e)
		if m < len(e):
			m = len(e)
	ans = ["┏"+"━"*m+"┓"]
	
	for i in range(len(l)):
		x = l[i]
		start = "┃"
		if i==0 and not initial:
			start = "┫"
		fill = " "
		end = "┃"
		if i == id:
			fill = "━"
			end = "╋"
		ans.append(start+x+(fill*(m-len(x)))+end)
		
	ans.append("┗"+"━"*m+"┛")
	return ans

def append_col(c1,c2,offset):
	if c1 == []:
		return c2
	if c2 == []:
		return c1
	N = max(len(c1),len(c2)+offset)
	empty_1 = " "*len(c1[0])
	empty_2 = " "*len(c2[0])
	for i in range(offset):
		c2 = [empty_2]+c2
	while len(c2)!=N:
		c2.append(empty_2)
	while len(c1)!=N:
		c1.append(empty_1)
	result = [""]*N
	for i in range(N):
		result[i]+=c1[i]+c2[i]
	return result

def render_list_aux(data):
	
	

	chain = []
	u = get_select()
	while u!=None:
		chain = [u]+chain
		u = u.parent
	
	# chain goes from root to select

	s_indices = [get_sibling_index(t_) for t_ in chain]
	offsets = [s_indices[0]]
	for i in range(1,len(chain)):
		offsets.append(offsets[i-1]+s_indices[i])

	def get_id(i):
		if i == len(chain)-1:
			return -1
		if len(chain[i+1].children)==0:
			return -1
		return get_sibling_index(chain[i+1])

	RENDER_LIST = []
	for i in range(len(chain)):
		t = chain[i]
		co = col(t.children,get_id(i),initial=(i==0))
		RENDER_LIST = append_col(RENDER_LIST,co,offsets[i])
	
	return RENDER_LIST
