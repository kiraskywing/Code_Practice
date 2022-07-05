class Node:
    def __init__(self, key, val):
        self.key, self.val = key, val
        self.prev = self.next = None
        self.freq = 1

class DList:
    def __init__(self):
        self.dummy = Node(-1, -1)
        self.dummy.prev = self.dummy.next = self.dummy
        self.size = 0
    
    def __len__(self):
        return self.size
    
    def append(self, node):
        tail = self.dummy.prev
        tail.next, node.prev = node, tail
        node.next, self.dummy.prev = self.dummy, node
        self.size += 1
    
    def pop(self, node=None):
        if len(self) == 0:
            return
        if not node:
            node = self.dummy.next
            
        prev_node, next_node = node.prev, node.next
        prev_node.next, next_node.prev = next_node, prev_node
        self.size -= 1
        
        return node

class LFUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.key_to_node = dict()
        self.freq_to_list = collections.defaultdict(DList)
        self.min_freq = 0

    def get(self, key: int) -> int:
        if key not in self.key_to_node:
            return -1
        
        node = self.key_to_node[key]
        self.updateFreq(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if self.capacity == 0:
            return
        if key in self.key_to_node:
            node = self.key_to_node[key]
            self.updateFreq(node)
            node.val = value
            return
        
        if len(self.key_to_node) == self.capacity:
            node = self.freq_to_list[self.min_freq].pop()
            del self.key_to_node[node.key]
            
        node = Node(key, value)
        self.key_to_node[key] = node
        self.freq_to_list[1].append(node)
        self.min_freq = 1
    
    def updateFreq(self, node):
        freq = node.freq
        self.freq_to_list[freq].pop(node)
        if freq == self.min_freq and len(self.freq_to_list[freq]) == 0:
            self.min_freq += 1
        
        freq += 1
        node.freq = freq
        self.freq_to_list[freq].append(node)


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)