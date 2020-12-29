class Solution:
    def reachNumber(self, target: int) -> int:
        total = steps = 0
        target = abs(target)
        
        while total < target:
            steps += 1
            total += steps
        while (total - target) % 2 != 0:
            steps += 1
            total += steps
        
        return steps