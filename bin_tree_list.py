
def binary_tree(root):
	return [root,[],[]]

def insert_left_child(root,node):
	# Insert a new list into the second position of the root list.
	value = root.pop(1)
	# If the list already has something in the second position,
	# push it down the tree as the left child of the new list 
	if len(value) > 1 :
		root.insert(1,[node,value,[]])
	else:
		root.insert(1,[node,[],[]])
	return root

def insert_right_child(root,node):
	# Insert a new list into the third position of the root list.
	value = root.pop(2)
	# If the list already has something in the second position,
	# push it down the tree as the right child of the new list 	
	if len(value) > 1 :
		root.insert(2,[node,[],value])
	else:
		root.insert(2,[node,[],[]])
	return root

def get_root_val(root):
	return root[0]

def set_root_val(root,value):
	root[0] = value
	
def get_left_clild(root):
	return root[1]
	
def get_right_child(root):
	return root[2]		

## Testing
r = binary_tree(1)
insert_left_child(r,2)
insert_right_child(r,3)
print get_root_val(r)
set_root_val(r,0)
print get_root_val(r)
print get_left_clild(r)
print get_right_child(r)


