class Solution:
    def slowestKey(self, releaseTimes: List[int], keysPressed: str) -> str:
        max_t, res = releaseTimes[0], keysPressed[0]
        
        for i in range(1, len(releaseTimes)):
            cur_t = releaseTimes[i] - releaseTimes[i - 1]
            if cur_t > max_t:
                max_t, res = cur_t, keysPressed[i]
            elif cur_t == max_t:
                res = max(res, keysPressed[i])
        
        return res