class Solution:
    def outerTrees(self, trees: List[List[int]]) -> List[List[int]]:
        trees.sort(key=lambda x : (x[0], x[1]))
        n = len(trees)
        res = []
        
        for i in range(n):
            while len(res) > 1 and self.orientation(res[-2], res[-1], trees[i]) < 0:
                res.pop()
            res.append(trees[i])
        
        if len(res) == n:
            return res
        
        for i in range(n - 2, -1, -1):
            while len(res) > 1 and self.orientation(res[-2], res[-1], trees[i]) < 0:
                res.pop()
            res.append(trees[i])
        res.pop()
        
        return res
    
    def orientation(self, o, a, b):
        return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])