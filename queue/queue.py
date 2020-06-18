from singly_linked_list import LinkedList
"""
A queue is a data structure whose primary purpose is to store and
return elements in First In First Out order. 

1. Implement the Queue class using an array as the underlying storage structure.
   Make sure the Queue tests pass.
2. Re-implement the Queue class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Queue tests pass.
3. What is the difference between using an array vs. a linked list when 
   implementing a Queue?
   
Stretch: What if you could only use instances of your Stack class to implement the Queue?
         What would that look like? How many Stacks would you need? Try it!
"""


class Queue:
    def __init__(self):
        self.size = 0
        # self.storage = ?
        self.storage = LinkedList()

    # returns the number of elements in the queue
    def __len__(self):
        current_node = self.storage.head
        self.size = 0
        while current_node:
            self.size += 1
            current_node = current_node.next_node
        return self.size

    # adds an element to the back of the queue
    def enqueue(self, value):
        self.storage.add_to_tail(value)

    # removes and returns the element at the front of the queue
    def dequeue(self):
        if self.__len__() > 0:
            return self.storage.remove_head()


"""
# array storage
class Queue:
    def __init__(self):
        self.size = 0
        # self.storage = ?
        self.storage = []

    # returns the number of elements in the queue
    def __len__(self):
        return len(self.storage)

    # adds an element to the back of the queue
    def enqueue(self, value):
        self.storage.append(value)

    # removes and returns the element at the front of the queue
    def dequeue(self):
        if len(self.storage) > 0:
            return self.storage.pop(0)
"""
