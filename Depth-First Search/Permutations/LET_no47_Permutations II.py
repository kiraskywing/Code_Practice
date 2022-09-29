class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []
        n = len(nums)
        self.dfs(collections.Counter(nums), n, [], res)
        return res
    
    def dfs(self, memo, n, temp, res):
        if len(temp) == n:
            res.append(temp[:])
            return
        
        for num in memo:
            if memo[num] > 0:
                 memo[num] -= 1
                 temp.append(num)
                 self.dfs(memo, n, temp, res)
                 temp.pop()
                 memo[num] += 1

class Solution2:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        # empty input => no
        # is nums sorted? => no
        
        # Approach: recursive DFS + queue
        # step1: convert input to queue
        # step2: In each recursive call, traverse all numbers in the queue and select one
        #        append the selected number into temp list, call next recursion
        #        Be aware that don't select the same number at the same recursion
        # recursion exit condidtion: 
        # all numbers has been selected. Deep copy the temp list to output list
        
        nums.sort()    # Time: O(nlog(n))
        queue = collections.deque(nums)    # Time & Space: O(n)
        res = []
        self.helper(queue, [], res)    # Total Time: O(n * n!)
        return res
    
    def helper(self, queue, temp, res):
        if len(queue) == 0:
            res.append(temp[:])    # Time & Space: O(n)
            return 
        
        prev = None
        for _ in range(len(queue)):    # Time: O(n)
            cur = queue.popleft()
            if prev is not None and prev == cur:
                queue.append(cur)
                continue
            
            temp.append(cur)
            self.helper(queue, temp, res)    # Time: O((n - 1)!)
            temp.pop()
            queue.append(cur)
            prev = cur