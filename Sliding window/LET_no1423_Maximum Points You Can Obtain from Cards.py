class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        size = len(cardPoints) - k
        minSubarraySum = cur = sum(cardPoints[:size])
        
        for i in range(len(cardPoints) - size):
            cur += cardPoints[i + size] - cardPoints[i]
            minSubarraySum = min(minSubarraySum, cur)
        
        return sum(cardPoints) - minSubarraySum