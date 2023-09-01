class Solution:
    def minBuildTime(self, blocks: List[int], split: int) -> int:
        heapq.heapify(blocks)
        while len(blocks) > 1:
            first, second = heapq.heappop(blocks), heapq.heappop(blocks)
            heapq.heappush(blocks, second + split)
        return heapq.heappop(blocks)