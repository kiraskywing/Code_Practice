class Leaderboard:

    def __init__(self):
        self.record = dict()

    def addScore(self, playerId: int, score: int) -> None:
        if playerId not in self.record:
            self.record[playerId] = score
        else:
            self.record[playerId] += score

    def top(self, K: int) -> int:
        temp = []
        for player in self.record:
            temp.append(self.record[player])
        temp.sort(reverse=True)

        return sum(temp[:K])

    def reset(self, playerId: int) -> None:
        del self.record[playerId]

# Your Leaderboard object will be instantiated and called as such:
# obj = Leaderboard()
# obj.addScore(playerId,score)
# param_2 = obj.top(K)
# obj.reset(playerId)