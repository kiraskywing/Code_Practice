class UndergroundSystem:

    def __init__(self):
        self.inId = collections.defaultdict(list)
        self.stations = collections.defaultdict(list)

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.inId[id] = (stationName, t)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        stationIn, tIn = self.inId[id]
        self.stations[(stationIn, stationName)].append((t - tIn))

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        return float(sum(self.stations[(startStation, endStation)]))/len(self.stations[(startStation, endStation)])


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)