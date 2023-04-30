class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        root = [i for i in range(n + 1)]
        res = e1 = e2 = 0
        
        for t, i, j in edges:
            if t == 3:
                if self.union(root, i, j):
                    e1 += 1
                    e2 += 1
                else:
                    res += 1
        
        root_copy = root[:]
        for t, i, j in edges:
            if t == 1:
                if self.union(root, i, j):
                    e1 += 1
                else:
                    res += 1
        
        root = root_copy
        for t, i, j in edges:
            if t == 2:
                if self.union(root, i, j):
                    e2 += 1
                else:
                    res += 1
        
        return res if e1 == e2 == n - 1 else -1
        
    
    def union(self, root, i, j):
        x, y = self.find(root, i), self.find(root, j)
        if x == y:
            return False
        root[x] = y
        return True
    
    def find(self, root, i):
        if i != root[i]:
            root[i] = self.find(root, root[i])
        return root[i]