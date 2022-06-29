class Solution:
    def maxBoxesInWarehouse(self, boxes: List[int], warehouse: List[int]) -> int:
        for i in range(1, len(warehouse)):
            warehouse[i] = min(warehouse[i - 1], warehouse[i])
            
        res = 0
        boxes.sort()
        for i in range(len(warehouse) - 1, -1, -1):
            if boxes[res] <= warehouse[i]:
                res += 1
                if res == len(boxes):
                    return res
                
        return res
        