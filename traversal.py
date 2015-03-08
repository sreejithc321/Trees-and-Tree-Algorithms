## Tree traversals

from bin_tree_class import BinaryTree

def preorder(tree):
    if tree :
        print ' ', tree.get_root_val()
        preorder(tree.get_left_child())
        preorder(tree.get_right_child())

def postorder(tree):
    if tree :
        postorder(tree.get_left_child())
        postorder(tree.get_right_child())
        print ' ', tree.get_root_val()

def inorder(tree):
	if tree :
		inorder(tree.get_left_child())
		print ' ', tree.get_root_val()
		inorder(tree.get_right_child())



r = BinaryTree('1')
r.insert_left_node('2')
l1 = r.get_left_child()
l1.insert_left_node('4')
l1.insert_right_node('5')
r.insert_right_node('3')
l2 = r.get_right_child()
l2.insert_right_node('6')

print "\nPreorder :\n",preorder(r)
print "\nPostrder :\n",postorder(r)
print "\nInorder :\n",inorder(r)
	
