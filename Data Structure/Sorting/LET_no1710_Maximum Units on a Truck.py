class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes.sort(key= lambda x: -x[1])
        res = 0
        for boxes, units in boxTypes:
            boxes = min(boxes, truckSize)
            res += boxes * units
            truckSize -= boxes
            if truckSize == 0:
                break
        
        return res