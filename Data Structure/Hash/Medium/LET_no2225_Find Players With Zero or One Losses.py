class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        loss_times = dict()
        for winner, losser in matches:
            loss_times[winner] = loss_times.get(winner, 0)
            loss_times[losser] = loss_times.get(losser, 0) + 1
        
        wins, losses = [], []
        for key, val in loss_times.items():
            if val == 0:
                wins.append(key)
            elif val == 1:
                losses.append(key)
        
        return [sorted(wins), sorted(losses)]