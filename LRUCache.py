class ListNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}  # Hashmap to store key-node mappings
        self.head = ListNode(None, None)  
        self.tail = ListNode(None, None)  
        self.head.next = self.tail
        self.tail.prev = self.head

    def _add_node(self, node: ListNode):
        # Add a node to the front of the linked list
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node

    def _remove_node(self, node: ListNode):
        # Remove a node from the linked list
        node.prev.next = node.next
        node.next.prev = node.prev

    def _move_to_front(self, node: ListNode):
        self._remove_node(node)
        self._add_node(node)

    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            self._move_to_front(node)
            return node.value
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            node.value = value
            self._move_to_front(node)
        else:
            if len(self.cache) >= self.capacity:
                del self.cache[self.tail.prev.key]
                self._remove_node(self.tail.prev)
            new_node = ListNode(key, value)
            self.cache[key] = new_node
            self._add_node(new_node)


cache = LRUCache(2)
cache.put(1, 1)
cache.put(2, 2)
print(cache.get(1))  # Output: 1 
cache.put(3, 3)
print(cache.get(2))  # Output: -1 
cache.put(4, 4)
print(cache.get(1))  # Output: -1 
print(cache.get(3))  # Output: 3 
print(cache.get(4))  # Output: 4 

