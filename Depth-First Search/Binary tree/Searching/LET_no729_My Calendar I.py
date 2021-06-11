class MyCalendar:
    def __init__(self):
        self.root = None

    def book(self, start: int, end: int) -> bool:
        if not self.root:
            self.root = Node(start, end)
            return True
        else:
            return self.root.insert(start, end)

class Node:
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.left = None
        self.right = None
    
    def insert(self, start, end):
        if self.start >= end:
            if not self.left:
                self.left = Node(start, end)
                return True
            else:
                return self.left.insert(start, end)
        elif start >= self.end:
            if not self.right:
                self.right = Node(start, end)
                return True
            else:
                return self.right.insert(start, end)
        else:
            return False
            
        
        
# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)