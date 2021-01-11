class Solution:
    def constructDistancedSequence(self, n: int) -> List[int]:
        arr = [0] * (2 * n - 1)
        used = [False] * (n + 1)
        self.dfs(arr, used, 0, n)
        return arr
    
    def dfs(self, arr, used, i, n):
        if i == len(arr):
            return True
        
        for num in range(n, 0, -1):
            if not self.is_valid(arr, used, num, i):
                continue
            
            arr[i] = num
            if num > 1: arr[i + num] = num
            used[num] = True
            
            next_i = i + 1
            while next_i < len(arr) and arr[next_i] != 0:
                next_i += 1
            
            if self.dfs(arr, used, next_i, n): return True
            
            arr[i] = 0
            if num > 1: arr[i + num] = 0
            used[num] = False
        
        return False
    
    def is_valid(self, arr, used, num, i):
        if arr[i] != 0 or used[num]:
            return False
        if num > 1 and (i + num > len(arr) - 1 or arr[i + num] != 0):
            return False
        return True