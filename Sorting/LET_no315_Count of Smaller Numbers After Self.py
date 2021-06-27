class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        smaller = [0] * len(nums)
        
        def helper(enum):
            mid = len(enum) // 2
            if mid > 0:
                left, right = helper(enum[:mid]), helper(enum[mid:])
                for i in range(len(enum))[::-1]:
                    if not right or left and left[-1][1] > right[-1][1]:
                        smaller[left[-1][0]] += len(right)
                        enum[i] = left.pop()
                    else:
                        enum[i] = right.pop()
            return enum
        
        helper(list(enumerate(nums)))
        return smaller