class Solution:
    def canReorderDoubled(self, arr: List[int]) -> bool:
        record = collections.Counter(arr)
        
        for num in sorted(record, key=abs):
            if record[num] > record[num * 2]:
                return False
            record[num * 2] -= record[num]
        
        return True