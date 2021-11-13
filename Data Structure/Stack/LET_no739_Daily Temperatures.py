class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        res = [0] * n
        stack = []
        
        for i, cur in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < cur:
                j = stack.pop()
                res[j] = i - j
            stack.append(i)
        
        return res