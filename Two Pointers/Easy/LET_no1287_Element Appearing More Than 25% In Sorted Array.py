class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        n = len(arr)
        lim = int(ceil(n / 4))
        left, right = 0, 1
        size, candidate = -1, -1
        while right < n:
            if arr[right] != arr[right - 1]:
                if right - left > size:
                    size = right - left
                    candidate = arr[left]
                left = right
            right += 1

        if right - left > size:
            candidate = arr[left]

        return candidate