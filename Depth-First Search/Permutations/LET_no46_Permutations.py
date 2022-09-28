class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # all input integers are unique
        # empty input? => no
        
        # Approach: recursive DFS
        # turn input list into queue
        # 1. In each recursive call, iterate through the given queue
        #    pop the number at the front of queue, append to temp list, call next recursion
        # 2. repeat step1 until all number has been used, append temp list to output list
        # 3. after returning from the next level recursion, pop the last number at temp list
        #    put it back to queue
        
        nums = collections.deque(nums)    # Time: O(n)
        res = []
        self.helper(nums, [], res)    # Time: O(n * n!)
        return res
    
    def helper(self, nums, temp, res):
        if len(nums) == 0:
            res.append(temp[:])    # Time: O(n), Space: O(n)
            return
        
        for _ in range(len(nums)):    # Time: O(n)
            cur = nums.popleft()
            temp.append(cur)
            self.helper(nums, temp, res)    # the time of the roop in the next recursion: O(n - 1)
            temp.pop()
            nums.append(cur)