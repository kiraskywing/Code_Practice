class Solution:
    def minOperations(self, target: List[int], arr: List[int]) -> int:
        table = {num: i for i, num in enumerate(target)}
        stack = []
        
        for num in arr:
            if num not in table: continue
            i = bisect.bisect_left(stack, table[num])
            if i == len(stack):
                stack.append(0)
            stack[i] = table[num]
        
        return len(target) - len(stack)