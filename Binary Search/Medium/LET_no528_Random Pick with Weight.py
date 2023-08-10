class Solution:
    # empty w? => no
    # input are positive integers
    
    # Approach:
    # 1. create an array of prefix sum:
    # e.g. w = [1, 2, 3, 4] => prefix_sum = [0, 1, 3, 6, 10]
    
    # 2. select a value randomly in the range 0 to 9
    # [0, 0]: idx = 0, [1, 2]: idx = 1, [3, 5]: idx = 2, [6, 9]: idx = 3
    
    # 3. find the lower bound using binary search
    # e.g. selected value = 4 => lower bound = 3 => return idx = 1
    
    def __init__(self, w: List[int]):
        self.prefix_sum = [0]
        for num in w:       # Time: O(n), Space: O(n)
            self.prefix_sum.append(self.prefix_sum[-1] + num)

    def pickIndex(self) -> int:
        value = random.randint(0, self.prefix_sum[-1] - 1)  # Time: O(1)
        return self.find_lower_bound(value)                 # Time: O(log(n))
        # return bisect.bisect_right(self.prefix_sum, value) - 1
    
    def find_lower_bound(self, target):                     # Time: O(log(n))
        left, right = 0, len(self.prefix_sum) - 1
        while left + 1 < right:
            mid = (left + right) // 2
            if self.prefix_sum[mid] >= target:
                right = mid
            else:
                left = mid
        
        return right if self.prefix_sum[right] <= target else left


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()