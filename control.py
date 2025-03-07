from conf import *
from task import *

with open(file_name) as f:
	data = populate_tree(json.loads(f.read()))

MODE = VIEW
select = data.children[0]

def edit_mode():
	global MODE
	if select.parent == None:
		return False
	MODE = EDIT
	return True

def view_mode():
	global MODE
	MODE = VIEW
	return  True

def get_mode():
	global MODE
	return MODE

def get_select():
	global select
	return select




def toggle_complete():
	global select
	if len(select.children) == 0 or all_leafs_complete(select):
		select.complete = not select.complete
		return True
	return False

def clean_quit():
	with open(file_name,"w") as f:
		json.dump(tree_to_dict(data),f,indent=4)

def child():
	global select
	if len(select.children) == 0:
		return False
	select = select.children[0]
	return True

def parent():
	global select
	if select.parent == None:
		return False
	if select.parent.parent == None:
		return False
	select = select.parent
	return True

def sibling(k):
	global select
	if select.parent == None:
		return
	p = select.parent
	ix = 0
	for i in range(len(p.children)):
		if p.children[i] == select:
			ix = i
			break
	ix+=k
	ix%=len(p.children)
	select = p.children[ix]

def create_child():
	global select
	t = Task()
	t.parent = select
	select.children = [t]+select.children
	select = t
	return True

def create_sibling(successor=False):
	global select
	p = select.parent
	if p==None:
		return False
	ix = 0
	for i in range(len(p.children)):
		if p.children[i] == select:
			ix = i
			break
	t = Task()
	t.parent = p
	if successor:
		p.children.insert(ix+1,t)
	else:
		p.children.insert(ix,t)
	select = t
	return True
		
def purge():
	global select
	if select.parent == None:
		return False
	p = select.parent
	new_children = []
	for c in p.children:
		if c!=select:
			new_children.append(c)
	p.children = new_children
	select = p
	return True