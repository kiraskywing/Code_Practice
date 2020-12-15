class Solution:
    def boxDelivering(self, boxes: List[List[int]], portsCount: int, maxBoxes: int, maxWeight: int) -> int:
        n = len(boxes)
        trips = j = last_j = 0
        dp = [0] + [sys.maxsize] * n    # dp[i] = minimum trips after finishing i tasks
        
        for i in range(n):    # start at i-indexed th task
            while j < n and maxBoxes > 0 and maxWeight >= boxes[j][1]:
                maxBoxes -= 1
                maxWeight -= boxes[j][1]
                if j == 0 or boxes[j][0] != boxes[j - 1][0]:
                    last_j = j
                    trips += 1
                j += 1
            
            dp[j] = min(dp[j], dp[i] + trips + 1)    # finish j tasks and go back to home
            dp[last_j] = min(dp[last_j], dp[i] + trips)    #finish j_last tasks and go back to home
            
            maxBoxes += 1
            maxWeight += boxes[i][1]
            if i == n - 1 or boxes[i][0] != boxes[i + 1][0]:
                trips -= 1
        
        return dp[-1]