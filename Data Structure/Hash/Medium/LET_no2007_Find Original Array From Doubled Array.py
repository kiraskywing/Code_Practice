class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        if len(changed) % 2 != 0:
            return []
        
        memo = collections.Counter(changed)
        if memo[0] % 2 != 0:
            return []
        
        for num in sorted(memo):
            if memo[num] > memo[num * 2]:
                return []
            memo[num * 2] -= memo[num] if num > 0 else memo[num] // 2
        
        return list(memo.elements())