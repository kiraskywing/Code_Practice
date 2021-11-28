class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        res = []
        self.dfs(res, [0], 0, graph)
        return res
    
    def dfs(self, res, temp, start, graph):
        if start == len(graph) - 1:
            res.append(temp[:])
            return
        
        for i in graph[start]:
            temp.append(i)
            self.dfs(res, temp, i, graph)
            temp.pop()