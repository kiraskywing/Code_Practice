class Solution:
    def slowestKey(self, releaseTimes: List[int], keysPressed: str) -> str:
        time, res = 0, ''
        releaseTimes = [0] + releaseTimes
        
        for i in range(1, len(releaseTimes)):
            diff = releaseTimes[i] - releaseTimes[i - 1]
            c = keysPressed[i - 1]
            if diff > time or diff == time and ord(c) - ord('a') > ord(res) - ord('a'):
                time = diff
                res = c
        
        return res