class Solution:
    def advantageCount(self, A: List[int], B: List[int]) -> List[int]:
        A.sort()
        record = collections.defaultdict(list)
        for b in sorted(B, reverse=True):
            if A[-1] > b:
                record[b].append(A.pop())
        
        return [(record[b] or A).pop() for b in B]