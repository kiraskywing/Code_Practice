class Solution:
    def isPossibleDivide(self, nums: List[int], k: int) -> bool:
        count = collections.defaultdict(int)
        for num in nums:
            count[num] += 1

        elem = sorted(count.keys())
        for num in elem:
            if count[num] > 0:
                base = count[num]
                for i in range(num, num + k):
                    count[i] -= base
                    if count[i] < 0:
                        return False
        return True