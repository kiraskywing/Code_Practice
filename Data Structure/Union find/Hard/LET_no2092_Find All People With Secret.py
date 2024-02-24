class UnionFind:
    def __init__(self, n):
        self.parent = [i for i in range(n)]

    def find(self, i):
        if self.parent[i] != i:
            self.parent[i] = self.find(self.parent[i])
        return self.parent[i]
    
    def union(self, i, j):
        pi, pj = self.find(i), self.find(j)
        if pi != pj:
            self.parent[pi] = self.parent[pj]

    def is_connected(self, i, j):
        return self.find(i) == self.find(j)

class Solution:
    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
        meetings.sort(key=lambda x : x[2])
        uf = UnionFind(n)
        uf.union(firstPerson, 0)

        i = 0
        while i < len(meetings):
            time = meetings[i][2]
            people = []
            while i < len(meetings) and meetings[i][2] == time:
                a, b, _ = meetings[i]
                uf.union(a, b)
                people.append(a)
                people.append(b)
                i += 1
            for p in people:
                if not uf.is_connected(p, 0):
                    uf.parent[p] = p
        
        res = []
        for i in range(n):
            if uf.is_connected(i, 0):
                res.append(i)
        
        return res
