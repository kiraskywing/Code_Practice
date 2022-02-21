class Node:
    def __init__(self, val):
        self.val = val
        self.prev, self.next = None, None

class FirstUnique:

    def __init__(self, nums: List[int]):
        self.dummy = Node(-1)
        self.tail = self.dummy
        self.memo = {}
        self.dups = set()
        for num in nums:
            self.add(num)

    def showFirstUnique(self) -> int:
        if self.dummy.next:
            return self.dummy.next.val
        return -1

    def add(self, value: int) -> None:
        if value in self.dups:
            return
        if value in self.memo:
            self.popTarget(value)
            return
        
        cur = Node(value)
        self.memo[value] = cur
        self.tail.next = cur
        cur.prev = self.tail
        cur.next = None
        self.tail = cur
    
    def popTarget(self, value):
        print(value, self.tail.val)
        cur = self.memo[value]
        del self.memo[value]
        self.dups.add(value)
        if cur is self.tail:
            self.tail = cur.prev
            self.tail.next = None
            return
        
        p, n = cur.prev, cur.next
        p.next = n
        n.prev = p
        


# Your FirstUnique object will be instantiated and called as such:
# obj = FirstUnique(nums)
# param_1 = obj.showFirstUnique()
# obj.add(value)