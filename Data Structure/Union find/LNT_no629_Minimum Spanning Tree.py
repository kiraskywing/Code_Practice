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
        self.count = 0
        res = []
        connections.sort(key=lambda x: (x.cost, x.city1, x.city2))  # 最短路徑排序

        for x in connections:  # 將所有結點生成根結點，記錄總結點數
            if x.city1 not in self.father:
                self.father[x.city1] = x.city1
                self.count += 1
            if x.city2 not in self.father:
                self.father[x.city2] = x.city2
                self.count += 1

        for y in connections:
            root_1 = self.find_root(y.city1)
            root_2 = self.find_root(y.city2)

            if root_1 != root_2:  # 判斷city1與city2是否會連到同一根結點
                self.father[root_1] = root_2  # 連接兩city表示兩者原本對應的根結點也會連接
                self.count -= 1  # 使用一條線
                res.append(y)

        if self.count == 1:  # n個結點用n-1條線
            return res
        return []

    def find_root(self, city):
        temp = []
        while self.father[city] != city:  # 使用此while找到根結點
            temp.append(city)
            city = self.father[city]
        for z in temp:  # 將所有經過結點都直接連到根結點
            self.father[z] = city

        return city  # 返回根結點