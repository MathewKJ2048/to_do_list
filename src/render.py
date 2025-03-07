from conf import *
from task import *
from control import *



def render(pad, data):
	pad.clear()
	RENDER_LIST = render_list(data)
	rs = get_render_string(RENDER_LIST)
	x, y = coordinates(RENDER_LIST)
	if SPECIAL in rs:
		rsl = re.split(SPECIAL+"+",rs)
		pad.addstr(rsl[0])
		special_color = curses.color_pair(1) if get_mode() == VIEW else curses.color_pair(2)
		pad.addstr(get_string(get_select()),special_color)
		pad.addstr(rsl[1])
	else:
		pad.addstr(rs)
	HEIGHT = curses.LINES
	WIDTH = curses.COLS
	minrow = max(0,y-HEIGHT+1)
	mincol = max(0,x-WIDTH+len(get_string(get_select()))+2)
	pad.refresh(minrow,mincol,0,0,HEIGHT-2,WIDTH-2)

def get_render_string(RENDER_LIST):
	s = ""
	for i in range(len(RENDER_LIST)):
		s+=RENDER_LIST[i]
		s+="\n"
	return s

def coordinates(RENDER_LIST):
	for y in range(len(RENDER_LIST)):
		for x in range(len(RENDER_LIST[y])):
			if RENDER_LIST[y][x]==SPECIAL:
				return (x,y)
	return (0,0)

def get_string(t):
	e = t.name
	if len(e)==0:
		e = " "
	if t.complete:
		e = len(e)*"-"
	return e

def col(lc,id,initial=False):
	if lc == []:
		return []

	l = []
	m = 0 # maximum length
	for c in lc:
		e = get_string(c)
		if get_select() == c:
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

def render_list(data):
	
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
