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

- traversal.py
