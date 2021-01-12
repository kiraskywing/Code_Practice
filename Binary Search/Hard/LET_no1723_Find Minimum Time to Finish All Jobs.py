class Solution:
    def minimumTimeRequired(self, jobs: List[int], k: int) -> int:
        n = len(jobs)
        jobs.sort(reverse=True)
        
        left, right = max(jobs), sum(jobs)
        while left + 1 < right:
            mid = (left + right) // 2
            cap = [mid] * k
            if self.dfs(jobs, cap, 0, mid):
                right = mid
            else:
                left = mid
        
        cap = [left] * k
        if self.dfs(jobs, cap, 0, left):
            return left
        return right
    
    def dfs(self, jobs, cap, i, mid):
        if i == len(jobs):
            return True
        
        for j in range(len(cap)):
            if cap[j] >= jobs[i]:
                cap[j] -= jobs[i]
                if self.dfs(jobs, cap, i + 1, mid):
                    return True
                cap[j] += jobs[i]
            if cap[j] == mid:
                break
        
        return False