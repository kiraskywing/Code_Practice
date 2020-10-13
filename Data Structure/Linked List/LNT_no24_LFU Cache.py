class KeyNode:
    def __init__(self, key, value, freq=1):
        self.key = key
        self.val = value
        self.freq = freq
        self.prev, self.next = None, None


class FreqNode:
    def __init__(self, freq):
        self.freq = freq
        self.prev, self.next = None, None
        self.first, self.last = None, None


class LFUCache:
    """
    @param: capacity: An integer
    """

    def __init__(self, capacity):
        self.capacity = capacity
        self.keyDict = dict()
        self.freqDict = dict()
        self.head = None

    """
    @param: key: An integer
    @param: value: An integer
    @return: nothing
    """

    def set(self, key, value):
        if self.capacity == 0:
            return
        if key in self.keyDict:
            self.increase(key, value)
            return
        if len(self.keyDict) == self.capacity:
            self.remove_kNode(self.head.last)
        self.insert_kNode(key, value)

    """
    @param: key: An integer
    @return: An integer
    """

    def get(self, key):
        if key in self.keyDict:
            kNode = self.keyDict[key]
            value = kNode.val
            self.increase(key, value)
            return value
        return -1

    """
    Methods are below.
    """

    def increase(self, key, value):
        kNode = self.keyDict[key]
        kNode.val = value
        fNode = self.freqDict[kNode.freq]
        next_fNode = fNode.next
        kNode.freq += 1

        if not next_fNode or next_fNode.freq > kNode.freq:
            next_fNode = self.insert_fNode(kNode.freq, fNode)

        self.unlink(kNode, fNode)
        self.link(kNode, next_fNode)

    def insert_kNode(self, key, value):
        kNode = KeyNode(key, value)
        self.keyDict[key] = kNode

        fNode = self.freqDict.get(1)

        if not fNode:
            fNode = FreqNode(1)
            fNode.next = self.head
            self.freqDict[1] = fNode
            if self.head:
                self.head.prev = fNode
            self.head = fNode

        self.link(kNode, fNode)

    def remove_kNode(self, kNode):
        self.unlink(kNode, self.freqDict[kNode.freq])
        del self.keyDict[kNode.key]

    def insert_fNode(self, freq, node):
        newNode = FreqNode(freq)
        newNode.prev, newNode.next = node, node.next
        self.freqDict[freq] = newNode

        if node.next:
            node.next.prev = newNode
        node.next = newNode
        return newNode

    def remove_fNode(self, fNode):
        prev, next = fNode.prev, fNode.next
        if prev:
            prev.next = next
        if next:
            next.prev = prev
        if self.head == fNode:
            self.head = next
        del self.freqDict[fNode.freq]

    def link(self, kNode, fNode):
        firstkNode = fNode.first
        kNode.prev, kNode.next = None, firstkNode

        if firstkNode:
            firstkNode.prev = kNode
        fNode.first = kNode
        if not fNode.last:
            fNode.last = kNode

    def unlink(self, kNode, fNode):
        prev, next = kNode.prev, kNode.next
        if prev:
            prev.next = next
        if next:
            next.prev = prev
        if fNode.first == kNode:
            fNode.first = next
        if fNode.last == kNode:
            fNode.last = prev
        if not fNode.first:
            self.remove_fNode(fNode)