class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        arr = [0] + arr
        res = [0] * len(arr)
        stack = [0]
        
        for right, num in enumerate(arr):
            while arr[stack[-1]] > num:
                stack.pop()
            left = stack[-1]
            res[right] = res[left] + (right - left) * arr[right]
            stack.append(right)
        
        return sum(res) % (10 ** 9 + 7)