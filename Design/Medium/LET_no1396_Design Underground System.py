class TimeNode:
    def __init__(self, name, t):
        self.station_name = name
        self.t = t

class TimeAvgNode:
    def __init__(self):
        self.total_time = 0
        self.count = 0

class UndergroundSystem:

    def __init__(self):
        self.in_memo = {}
        self.avg_time_memo = {}

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.in_memo[id] = (stationName, t)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        in_station, start_t = self.in_memo[id]
        tag = in_station + "->" + stationName
        if tag not in self.avg_time_memo:
            self.avg_time_memo[tag] = TimeAvgNode()
        self.avg_time_memo[tag].total_time += (t - start_t)
        self.avg_time_memo[tag].count += 1

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        tag = startStation + "->" + endStation
        return self.avg_time_memo[tag].total_time / self.avg_time_memo[tag].count


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)