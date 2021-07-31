class MapSum:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.record = collections.defaultdict(int)
        self.root = TrieNode()
        
    def insert(self, key: str, val: int) -> None:
        diff = val - self.record[key]
        cur = self.root
        for c in key:
            cur = cur.child[c]
            cur.total += diff
        self.record[key] = val

    def sum(self, prefix: str) -> int:
        cur = self.root
        for c in prefix:
            if c not in cur.child:
                return 0
            cur = cur.child[c]
        return cur.total

class TrieNode:
    def __init__(self):
        self.child = collections.defaultdict(TrieNode)
        self.total = 0


# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)