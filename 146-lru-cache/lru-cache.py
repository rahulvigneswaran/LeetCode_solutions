class Node:
    def __init__(self, key, val):
        self.val = val
        self.key = key
        self.next = None
        self.prev = None
    
class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        
        # LEFT: LRU, RIGHT: MRU
        self.LEFT = Node(0, 0)
        self.RIGHT = Node(0, 0)
        self.LEFT.next = self.RIGHT
        self.RIGHT.prev = self.LEFT
        
        #cache
        self.cache = {}

    def remove(self, node):
        previous_node, next_node = node.prev, node.next
        previous_node.next, next_node.prev = next_node, previous_node
    
    def insert(self, node):
        old_right = self.RIGHT.prev
        old_right.next, node.prev = node, old_right
        self.RIGHT.prev, node.next = node, self.RIGHT


    def get(self, key: int) -> int:
        if key in self.cache:
            # update recency
            self.remove(self.cache[key])
            self.insert(self.cache[key])

            return self.cache[key].val
        
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
            del self.cache[key]
        
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])

        if len(self.cache) > self.capacity:
            del self.cache[self.LEFT.next.key]
            self.remove(self.LEFT.next)
            


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)