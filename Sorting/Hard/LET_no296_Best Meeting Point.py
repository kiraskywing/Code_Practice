class Solution:
    def minTotalDistance(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        rows = [i for i in range(m) for j in range(n) if grid[i][j] == 1]
        cols = [j for i in range(m) for j in range(n) if grid[i][j] == 1]
        
        mid_i = self.get_median(rows)
        mid_j = self.get_median(cols)
        dist = sum(abs(i - mid_i) for i in rows) + sum(abs(j - mid_j) for j in cols)
        
        return dist
    
    def get_median(self, arr):
        n = len(arr)
        if n % 2 != 0:
            return self.find_kth(arr, 0, n - 1, n // 2)
        
        return (self.find_kth(arr, 0, n - 1, n // 2 - 1) + self.find_kth(arr, 0, n - 1,  n // 2)) // 2
    
    def find_kth(self, arr, left, right, k):
        if left == right:
            return arr[left]
        
        pivot = arr[randint(left, right)]
        i, j = left, right
        while i <= j:
            while i <= j and arr[i] < pivot:
                i += 1
            while i <= j and arr[j] > pivot:
                j -= 1
            if i <= j:
                arr[i], arr[j] = arr[j], arr[i]
                i += 1
                j -= 1
                
        if k <= j:
            return self.find_kth(arr, left, j, k)
        elif k >= i:
            return self.find_kth(arr, i, right, k)
        return arr[k]