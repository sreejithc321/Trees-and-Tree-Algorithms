
# Min heap : smallest key is always at the front
# Implementation on min heap using lists
# Left child of a parent (at position p) is the node that is found in position 2p in the list
# Right child of the parent is at position 2p+1 in the list.
# For a node at position n in the list, the parent is at position n/2.
# Heap order property : for every node x with parent p, the key in p is smaller than or equal to the key in x

class BinHeap:

    def __init__(self):
        self.heap_list = [0]
        self.current_size = 0

    def pos_up(self,i):
		# Apply heap oder property
        while i // 2 > 0:
          if self.heap_list[i] < self.heap_list[i // 2]:
             tmp = self.heap_list[i // 2]
             self.heap_list[i // 2] = self.heap_list[i]
             self.heap_list[i] = tmp
          i = i // 2

    def insert(self,item):
	  # Add new item to end of list 	
      self.heap_list.append(item)
      self.current_size = self.current_size + 1
      # Find exact position
      self.pos_up(self.current_size)

    def pos_down(self,i):
	  # Pushing the new root node down the tree to its proper position 
	  # Repeat the swapping process with a node and its children until the node is 
	  # swapped into a position on the tree where it is already less than both children
      while (i * 2) <= self.current_size:
          min_val = self.minChild(i)
          if self.heap_list[i] > self.heap_list[min_val]:
              tmp = self.heap_list[i]
              self.heap_list[i] = self.heap_list[min_val]
              self.heap_list[min_val] = tmp
          i = min_val

    def minChild(self,i):
      if i * 2 + 1 > self.current_size:
          return i * 2
      else:
          if self.heap_list[i*2] < self.heap_list[i*2+1]:
              return i * 2
          else:
              return i * 2 + 1

    def del_min(self):
      retval = self.heap_list[1]
      self.heap_list[1] = self.heap_list[self.current_size]
      self.current_size = self.current_size - 1
      self.heap_list.pop()
      self.pos_down(1)
      return retval

    def build_heap(self,num_list):
      i = len(num_list) // 2
      self.current_size = len(num_list)
      self.heap_list = [0] + num_list[:]
      while (i > 0):
          self.pos_down(i)
          i = i - 1


bh = BinHeap()
bh.build_heap([9,5,6,2,3])
print(bh.del_min())
print(bh.del_min())
print(bh.del_min())
print(bh.del_min())
print(bh.del_min())
