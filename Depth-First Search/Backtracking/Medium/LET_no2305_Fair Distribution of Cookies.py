class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        self.res = float('inf')
        bag = [0] * k
        self.helper(cookies, 0, bag, k)
        return self.res
    
    def helper(self, cookies, i, bag, k):
        if i == len(cookies):
            self.res = min(self.res, max(bag))
            return
        
        if self.res < max(bag):
            return
        
        for j in range(k):
            bag[j] += cookies[i]
            self.helper(cookies, i + 1, bag, k)
            bag[j] -= cookies[i]