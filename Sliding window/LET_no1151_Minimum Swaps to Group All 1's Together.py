class Solution:
    def minSwaps(self, data: List[int]) -> int:
        ones = sum(data)
        cur = sum(data[i] for i in range(ones - 1))
        max_ones = cur
        left = 0
        
        for right in range(ones - 1, len(data)):
            cur += data[right]
            max_ones = max(max_ones, cur)
            if max_ones == ones:
                return 0
            cur -= data[left]
            left += 1
        
        return ones - max_ones