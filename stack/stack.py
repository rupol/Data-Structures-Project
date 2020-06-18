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

    # returns the number of elements in the stack
    def __len__(self):
        current_node = self.storage.head
        self.size = 0
        while current_node:
            self.size += 1
            current_node = current_node.next_node
        return self.size

    # adds an item to the top of the stack.
    def push(self, value):
        self.storage.add_to_tail(value)

    # removes and returns the element at the top of the stack
    def pop(self):
        if self.__len__() > 0:
            return self.storage.remove_tail()


"""
# array storage
class Stack:
    def __init__(self):
        self.size = 0
        # self.storage = ?
        self.storage = []

    # returns the number of elements in the stack
    def __len__(self):
        return len(self.storage)

    # adds an item to the top of the stack.
    def push(self, value):
        self.storage.append(value)

    # removes and returns the element at the top of the stack
    def pop(self):
        if len(self.storage) > 0:
            return self.storage.pop()
"""
