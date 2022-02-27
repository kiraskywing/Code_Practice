class Solution:
    def minimumFinishTime(self, tires: List[List[int]], changeTime: int, numLaps: int) -> int:
        go_straight = [float('inf') for _ in range(19)]
        for f, r in tires:
            total = base = f
            go_straight[1] = min(go_straight[1], total)
            for i in range(2, 19):
                base *= r
                total += base
                if total > 2e5:
                    break
                go_straight[i] = min(go_straight[i], total)
        
        laps = [0 for _ in range(numLaps + 1)]
        for i in range(1, numLaps + 1):
            laps[i] = go_straight[i] if i < 19 else float('inf')
            for j in range(1, min(19, i // 2 + 1)):
                laps[i] = min(laps[i], laps[j] + changeTime + laps[i - j])
        
        return laps[-1]