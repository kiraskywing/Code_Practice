class Solution:
    def canFormArray(self, arr: List[int], pieces: List[List[int]]) -> bool:
        record = {piece[0]: piece for piece in pieces}
        
        i = 0
        while i < len(arr):
            if arr[i] in record:
                num = arr[i]
                for j in range(len(record[num])):
                    if arr[i] != record[num][j]:
                        return False
                    i += 1
            else: return False
        return True