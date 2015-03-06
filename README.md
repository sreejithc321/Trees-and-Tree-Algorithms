## Tree

A tree consists of a set of nodes and a set of edges that connect pairs of nodes. A tree has the following properties:
- One node of the tree is designated as the root node.
- Every node n, except the root node, is connected by an edge from exactly one other node p, where p is the parent of n.
- A unique path traverses from the root to each node.

## Binary Tree

If each node in the tree has a maximum of two children, we say that the tree is a binary tree.

### Implementation of Binary Tree using lists
- bin_tree_list.py

### Implementation of Binary Tree as class
- bin_tree_class.py

## Tree Traversals
- traversal.py
### Pre-order
    - Display the data part of root element (or current element)
    - Traverse the left subtree by recursively calling the pre-order function.
    - Traverse the right subtree by recursively calling the pre-order function.
### In-order (symmetric)
    - Traverse the left subtree by recursively calling the in-order function.
    - Display the data part of root element (or current element).
    - Traverse the right subtree by recursively calling the in-order function.
### Post-order
    - Traverse the left subtree by recursively calling the post-order function.
    - Traverse the right subtree by recursively calling the post-order function.
    - Display the data part of root element (or current element).

## Binary Heap

In a heap, for every node x with parent p, the key in p is smaller than or equal to the key in x (heap order property)
A binary heap perform both enqueue and dequeue items in O(logn)

- BinaryHeap() creates a new, empty, binary heap.
- insert(item) adds a new item to the heap.
- find_min() returns the item with the minimum key value, leaving item in the heap.
- del_min() returns the item with the minimum key value, removing the item from the heap.
- is_empty() returns true if the heap is empty, false otherwise.
- size() returns the number of items in the heap.
- build_heap(list) builds a new heap from a list of keys.

### Binary Heap Implementation (min heap)
- bin_heap.py
