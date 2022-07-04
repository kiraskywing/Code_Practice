class Solution:
    def highFive(self, items: List[List[int]]) -> List[List[int]]:
        memo = collections.defaultdict(list)
        for ID, score in items:
            heapq.heappush(memo[ID], score)
            if len(memo[ID]) > 5:
                heapq.heappop(memo[ID])
        
        return [[ID, sum(memo[ID]) // 5] for ID in sorted(memo)]