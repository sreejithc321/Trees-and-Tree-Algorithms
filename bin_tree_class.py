
class BinaryTree():
	
	def __init__(self,root):
		self.key = root
		self.right_child = None
		self.left_child = None
		
	def set_root_val(self,value):
		self.key = value
		
	def insert_right_node(self,value):
		if self.right_child == None :
			self.right_child = BinaryTree(value)
		else:
			new_node = BinaryTree(value)
			new_node.right_child = self.right_child
			self.right_child = new_node
			
	def insert_left_node(self,value):
		if self.left_child == None :
			self.left_child = BinaryTree(value)
		else:
			new_node = BinaryTree(value)
			new_node.left_child = self.left_child
			self.left_child = new_node
		
	def get_left_child(self):
		return self.left_child
		
	def get_right_child(self):
		return self.right_child
		
	def get_root_val(self):
		return self.key				


# Testing
if __name__ =='__main__':
	r = BinaryTree('a')
	print r.get_root_val()
	print(r.get_left_child())
	r.insert_left_node('b')
	print(r.get_left_child())
	print(r.get_left_child().get_root_val())

	r.insert_right_node('c')
	print(r.get_right_child())
	print(r.get_right_child().get_root_val())

	r.get_right_child().set_root_val('test')
	print(r.get_right_child().get_root_val())

