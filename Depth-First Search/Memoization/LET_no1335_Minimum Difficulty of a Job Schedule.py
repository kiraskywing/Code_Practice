class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        if len(jobDifficulty) < d:
            return -1
        
        return self.helper(jobDifficulty, 0, d, dict())
    
    def helper(self, arr, start, left, memo):
        if (start, left) not in memo:
            difficulty = float('-inf')
            cur = float('inf')
            
            if left == 1:
                cur = max(arr[start:])
            else:
                for i in range(start, len(arr) - left + 1):
                    difficulty = max(difficulty, arr[i])
                    cur = min(cur, difficulty + self.helper(arr, i + 1, left - 1, memo))
            memo[(start, left)] = cur
        
        return memo[(start, left)]