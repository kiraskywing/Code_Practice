class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        memo = collections.Counter(tasks)
        res = 0
        
        # If freq = 1, not possible, return -1
        # If freq = 2, needs one 2-tasks
        # If freq = 3, needs one 3-tasks
        # If freq = 3k, freq = 3 * k, needs k batchs.
        # If freq = 3k + 1, freq = 3 * (k - 1) + 2 + 2, needs k + 1 batchs.
        # If freq = 3k + 2, freq = 3 * k + 2, needs k + 1 batchs.
        
        for _, val in memo.items():
            if val < 2:
                return -1
            res += (val + 2) // 3
            
        return res