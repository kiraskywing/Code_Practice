class Solution:
    def findSmallestRegion(self, regions: List[List[str]], region1: str, region2: str) -> str:

        memo = {}
        for region in regions:
            for place in region[1:]:
                memo[place] = region[0]

        l1, l2 = 0, 0
        r1, r2 = region1, region2

        while r1 in memo:
            l1 += 1
            r1 = memo[r1]
        while r2 in memo:
            l2 += 1
            r2 = memo[r2]

        r1, r2 = region1, region2
        for _ in range(max(0, l1 - l2)):
            r1 = memo[r1]
        for _ in range(max(0, l2 - l1)):
            r2 = memo[r2]

        while r1 != r2:
            r1 = memo[r1]
            r2 = memo[r2]

        return r1
