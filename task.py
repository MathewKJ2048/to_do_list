class Task:
	def __init__(self):
		self.name = ""
		self.children = []
		self.parent = None
		self.complete = False
	def stringify(self):
		s = self.name
		if len(self.children)==0:
			return s
		s+="{"
		for c in self.children:
			s+=c.stringify()
		s+="}"
		return s

def populate_tree(data): # type of data is json object with exactly one key
	t = Task()
	x = list(data.keys())[0]
	t.name = x
	for u in data[x]:
		child = populate_tree(u)
		child.parent = t
		t.children.append(child)
	return t
		
def tree_to_dict(task):
	l = []
	for c in task.children:
		if not c.complete:
			l.append(tree_to_dict(c))
	return {
		task.name:l
	}

def all_leafs_complete(task):
	# base case if task is leaf
	if len(task.children)==0 and not task.complete:
		return False
	# inductive case for non-leaves
	result = True
	for c in task.children:
		result = result and all_leafs_complete(c)
	return result

def get_size(task):
	sum = 1
	for c in task.children:
		sum+=get_size(c)
	return sum

def get_index(task):
	if task.parent == None:
		return 0
	index = get_index(task.parent)+1
	for c in task.parent.children:
		if c == task:
			break
		index+=get_size(c)
	return index

def get_sibling_index(task):
	if task.parent == None:
		return 0
	p = task.parent
	for i in range(len(p.children)):
		if p.children[i]==task:
			return i
	return 0