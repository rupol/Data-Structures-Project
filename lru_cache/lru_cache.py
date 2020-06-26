from doubly_linked_list import DoublyLinkedList


class LRUCache:
    """
    Our LRUCache class keeps track of the max number of nodes it
    can hold, the current number of nodes it is holding, a doubly-
    linked list that holds the key-value entries in the correct
    order, as well as a storage dict that provides fast access
    to every node stored in the cache.
    """

    def __init__(self, limit=3):
        self.limit = limit
        # holds key, value pairs
        self.storage = {}
        # holds keys as nodes in correct order
        self.ordered = DoublyLinkedList()

    """
    Retrieves the value associated with the given key. Also
    needs to move the key-value pair to the end of the order
    such that the pair is considered most-recently used.
    Returns the value associated with the key or None if the
    key-value pair doesn't exist in the cache.
    """

    def get(self, key):
        # return value in storage dict
        value = self.storage.get(key)
        # find value in ordered list
        node = self.ordered.contains(value)
        if node is not None:
            # move node to back of list
            self.ordered.move_to_end(node)
        return value

    """
    Adds the given key-value pair to the cache. The newly-
    added pair should be considered the most-recently used
    entry in the cache. If the cache is already at max capacity
    before this entry is added, then the oldest entry in the
    cache needs to be removed to make room. Additionally, in the
    case that the key already exists in the cache, we simply
    want to overwrite the old value associated with the key with
    the newly-specified value.
    """

    def set(self, key, value):
        # add key value pair to storage
        # if key exists, overwrite value
        new_pair = {key: value}
        self.storage.update(new_pair)

        # add value to back of ordered list
        self.ordered.add_to_tail(value)
        # if length of ordered list and storage is > limit
        if len(self.ordered) > self.limit and len(self.storage) > self.limit:
            # remove front of ordered list
            value = self.ordered.remove_from_head()
            # remove from dictionary
            self.storage = {k: v for k,
                            v in self.storage.items() if v != value}


cache = LRUCache(3)
cache.set('item1', 'a')
cache.set('item2', 'b')
cache.set('item3', 'c')
# print(len(cache.ordered))
print(len(cache.storage))
print(cache.storage)
cache.set('item2', 'z')
print(cache.storage)
# print(cache.get('item1'))
# print(len(cache.ordered))
