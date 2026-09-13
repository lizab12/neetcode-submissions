class Node:
    def __init__(self, key=0, value=0):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}

        self.right = Node()
        self.left = Node()

        self.right.prev = self.left
        self.left.next = self.right
    
    def remove(self, node):
        p_node = node.prev
        n_node = node.next

        p_node.next = n_node
        n_node.prev = p_node

    def add(self, node):
        p_node = self.right.prev
        p_node.next = node
        node.prev = p_node
        node.next = self.right
        self.right.prev = node
        

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        node = self.cache[key]
        self.remove(node)
        self.add(node)

        return node.value
        

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            node.value = value
            self.remove(node)
            self.add(node)
        else:
            node = Node(key, value)
            self.cache[key]=node

            self.add(node)
            if len(self.cache)>self.capacity:
                lru = self.left.next
                self.remove(lru)

                del self.cache[lru.key]
        
