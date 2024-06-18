class Solution:
    def maxBoxesInWarehouse(self, boxes: List[int], warehouse: List[int]) -> int:
        left, right = 0, len(warehouse) - 1
        res = 0
        boxes.sort(reverse=True)

        for item in boxes:
            if left <= right:
                if item <= warehouse[left]:
                    left += 1
                    res += 1
                elif item <= warehouse[right]:
                    right -= 1
                    res += 1
            else:
                break
        
        return res
