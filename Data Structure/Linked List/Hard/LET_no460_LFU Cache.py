class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.freq = 1
        self.prev = self.next = None

class DLinkedList:
    def __init__(self):
        self.dummy = Node(-1, -1)
        self.dummy.next = self.dummy.prev = self.dummy
        self.size = 0
    
    def __len__(self):
        return self.size
    
    def append(self, node):
        tail = self.dummy.prev
        node.prev = tail
        tail.next = node
        node.next = self.dummy
        self.dummy.prev = node
        self.size += 1
    
    def pop(self, node=None):
        if self.size == 0:
            return
        
        if not node:
            node = self.dummy.next

        prevNode, nextNode = node.prev, node.next
        prevNode.next = nextNode
        nextNode.prev = prevNode
        self.size -= 1
        
        return node
        
class LFUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        
        self.kMemo = dict() # key: Node
        self.fMemo = collections.defaultdict(DLinkedList)
        self.minFreq = 0
        
        
    def update(self, node):
        freq = node.freq
        
        self.fMemo[freq].pop(node)
        if self.minFreq == freq and not self.fMemo[freq]:
            self.minFreq += 1
        
        freq2 = freq + 1
        node.freq = freq2
        self.fMemo[freq2].append(node)
    
    def get(self, key):
        if key not in self.kMemo:
            return -1
        
        node = self.kMemo[key]
        self.update(node)
        return node.val

    def put(self, key, value):
        if self.capacity == 0:
            return
        
        if key in self.kMemo:
            node = self.kMemo[key]
            self.update(node)
            node.val = value
            return
        
        if len(self.kMemo) == self.capacity:
            node = self.fMemo[self.minFreq].pop()
            del self.kMemo[node.key]
            
        node = Node(key, value)
        self.kMemo[key] = node
        self.fMemo[1].append(node)
        self.minFreq = 1