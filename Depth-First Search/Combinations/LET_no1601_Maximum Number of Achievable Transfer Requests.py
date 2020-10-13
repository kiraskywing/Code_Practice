class Solution:
    def maximumRequests(self, n: int, requests: List[List[int]]) -> int:
        self.ans = 0
        count = [0] * n
        self.dfs(requests, 0, count, 0)
        return self.ans
    
    def dfs(self, requests, index, count, num):
        if index == len(requests):
            for i in count:
                if i != 0:
                    return
            self.ans = max(self.ans, num)
            return
        
        count[requests[index][0]] -= 1
        count[requests[index][1]] += 1
        self.dfs(requests, index + 1, count, num + 1)
        count[requests[index][0]] += 1
        count[requests[index][1]] -= 1
        
        self.dfs(requests, index + 1, count, num)