class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        ans = []
        for i in range(1, 10):
            start, num = i, i
            while num <= high and start < 10:
                if num >= low:
                    ans.append(num)
                start += 1
                num = num * 10 + start
        return sorted(ans)