class Task:
	def __init__(self):
		self.name = ""
		self.children = []
		self.parent = None
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
		l.append(tree_to_dict(c))
	return {
		task.name:l
	}

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