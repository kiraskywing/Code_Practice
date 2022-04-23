class Node:
    def __init__(self):
        self.children = collections.defaultdict(Node)
        self.value = -1

class FileSystem:

    def __init__(self):
        self.root = Node()

    def createPath(self, path: str, value: int) -> bool:
        items = path.split('/')
        if not items:
            return False
        
        cur = self.root
        for item in items[1:-1]:
            if item not in cur.children:
                return False
            cur = cur.children[item]
        
        if items[-1] in cur.children:
            return False
        cur = cur.children[items[-1]]
        cur.value = value
        return True

    def get(self, path: str) -> int:
        items = path.split('/')
        if not items:
            return -1
        
        cur = self.root
        for item in items[1:]:
            if item not in cur.children:
                return -1
            cur = cur.children[item]
        return cur.value


# Your FileSystem object will be instantiated and called as such:
# obj = FileSystem()
# param_1 = obj.createPath(path,value)
# param_2 = obj.get(path)