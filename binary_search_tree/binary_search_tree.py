"""
Binary search trees are a data structure that enforce an ordering over
the data they store. That ordering in turn makes it a lot more efficient
at searching for a particular piece of data in the tree.

This part of the project comprises two days:
1. Implement the methods `insert`, `contains`, `get_max`, and `for_each`
   on the BSTNode class.
2. Implement the `in_order_print`, `bft_print`, and `dft_print` methods
   on the BSTNode class.
"""


class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        new_node = BSTNode(value)
        # if BST is empty
        if self.value is None:
            self.value = new_node

        # take the current value of our node (self.value) and compare to the new value we want to insert
        # if new value < self.value
        if value < self.value:
            # if self.left is empty, set left to the value
            if self.left is None:
                self.left = new_node
            # if self.left is already taken by a node
            else:
                # make that node call insert
                self.left.insert(value)

        # if new value >= self.value
        else:
            # if self.right is empty, set right to the value
            if self.right is None:
                self.right = new_node
            # if self.right is already taken by a node
            else:
                # make that node call insert
                self.right.insert(value)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        # if target is equal to the root
        if self.value == target:
            return True
        found = False
        if target < self.value:
            # check left subtree
            # if you can't go left, return false
            if self.left is None:
                return False
            # if there's a node, make that node call contains
            found = self.left.contains(target)
        if target > self.value:
            # check right subtree
            # if you can't go right, return false
            if self.right is None:
                return False
            # if there's a node, make that node call contains
            found = self.right.contains(target)
        return found

    # Return the maximum value found in the tree
    def get_max(self):
        current_node = self
        # while a node exists to the right, move down the tree to the right
        while(current_node.right):
            current_node = current_node.right
        # the max is the furthest right node
        return current_node.value

    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        # call the function on the current node
        fn(self.value)
        # if there is a left node
        if self.left is not None:
            # make that node call for_each
            self.left.for_each(fn)
        # if there is a right node
        if self.right is not None:
            # make that node call for_each
            self.right.for_each(fn)

    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        pass

    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass
