class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack, table = [], {}
        for n in nums2:
            while stack and stack[-1] < n:
                table[stack.pop()] = n
            stack.append(n)
        res = []
        for n in nums1:
            res.append(table.get(n, -1))
        return res