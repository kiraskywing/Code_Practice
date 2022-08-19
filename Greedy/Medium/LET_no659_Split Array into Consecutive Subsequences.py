class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        memo = collections.Counter(nums)
        valid_sequences = collections.defaultdict(int)
        for num in nums:
            if memo[num] == 0:
                continue
            memo[num] -= 1
            if valid_sequences[num - 1] > 0:
                valid_sequences[num - 1] -= 1
                valid_sequences[num] += 1
            elif memo[num + 1] > 0 and memo[num + 2] > 0:
                memo[num + 1] -= 1
                memo[num + 2] -= 1
                valid_sequences[num + 2] += 1
            else:
                return False
        
        return True