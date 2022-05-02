'''
Definition for a Connection
class Connection:

    def __init__(self, city1, city2, cost):
        self.city1, self.city2, self.cost = city1, city2, cost
'''
class Solution:
    # @param {Connection[]} connections given a list of connections
    # include two cities and cost
    # @return {Connection[]} a list of connections from results
    def lowestCost(self, connections):
        if not connections:
            return []

        self.father = {}
        nodes = 0
        res = []
        connections.sort(key=lambda x: (x.cost, x.city1, x.city2))  # 最短路徑排序            

        for edge in connections:
            if edge.city1 not in self.father:
                self.father[edge.city1] = edge.city1
                nodes += 1
            if edge.city2 not in self.father:
                self.father[edge.city2] = edge.city2
                nodes += 1

            root_1 = self.find_root(edge.city1)
            root_2 = self.find_root(edge.city2)

            if root_1 != root_2:  # 判斷city1與city2是否會連到同一根結點
                self.father[root_1] = root_2  # 連接兩city表示兩者原本對應的根結點也會連接
                nodes -= 1  # 使用一條線
                res.append(edge)

        if nodes == 1:  # n個結點用n-1條線
            return res
        return []

    def find_root(self, city):
        if self.father[city] != city:
            self.father[city] = self.find_root(self.father[city])
        
        return self.father[city]