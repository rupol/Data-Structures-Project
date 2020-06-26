from singly_linked_list import LinkedList
"""
A stack is a data structure whose primary purpose is to store and
return elements in Last In First Out order. 

1. Implement the Stack class using an array as the underlying storage structure.
   Make sure the Stack tests pass.
2. Re-implement the Stack class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Stack tests pass.
3. What is the difference between using an array vs. a linked list when 
   implementing a Stack?
"""


class Stack:
    def __init__(self):
        self.size = 0
        # self.storage = ?
        self.storage = LinkedList()

    # returns the number of elements in the stack (dunder function)
    def __len__(self):
        return self.size

    # adds an item to the top of the stack.
    def push(self, value):
        self.size += 1
        self.storage.add_to_head(value)

    # removes and returns the element at the top of the stack
    def pop(self):
        if self.size == 0:
            return None
        # remove the first element in storage
        self.size -= 1
        node = self.storage.remove_head()
        return node


"""
# array storage
class Stack:
    def __init__(self):
        self.size = 0
        # self.storage = ?
        self.storage = []

    # returns the number of elements in the stack (dunder function)
    def __len__(self):
        return self.size

    # adds an item to the top of the stack.
    def push(self, value):
        self.size += 1
        self.storage.insert(0, value)

    # removes and returns the element at the top of the stack
    def pop(self):
        if len(self.storage) == 0:
            return None
        # remove the first element in storage
        self.size -= 1
        node = self.storage.pop(0)
        return node
"""
