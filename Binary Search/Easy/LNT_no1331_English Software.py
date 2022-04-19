from typing import (
    List,
)

class Solution:
    """
    @param score: Each student's grades
    @param ask: A series of inquiries
    @return: Find the percentage of each question asked
    """
    def english_software(self, score: List[int], ask: List[int]) -> List[int]:
        sorted_score = sorted(score)
        return [self.helper(sorted_score, score[i - 1]) for i in ask]
    
    def helper(self, scores, target):
        n = len(scores)
        left, right = 0, n - 1
        while left + 1 < right:
            mid = (left + right) // 2
            if scores[mid] <= target:
                left = mid
            else:
                right = mid
        
        if scores[right] == target:
            return right * 100 // n
        return left * 100 // n