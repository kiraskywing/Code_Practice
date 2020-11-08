class Solution:
    def maximizeSweetness(self, sweetness: List[int], K: int) -> int:

        left, right = 1, sum(sweetness) // (K + 1)

        while left < right:
            mid = (left + right) // 2 + 1
            cur, cuts = 0, 0

            for i in sweetness:
                cur += i
                if cur >= mid:
                    cuts += 1
                    cur = 0

            if cuts >= K + 1:
                left = mid
            else:
                right = mid - 1

        return right