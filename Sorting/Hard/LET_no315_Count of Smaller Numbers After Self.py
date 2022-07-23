class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [0] * n
        temp = [None] * n
        arr = [(num, i) for i, num in enumerate(nums)]
        self.mergeSort(arr, temp, res, 0, n - 1)
        return res
    
    def mergeSort(self, arr, temp, res, left, right):
        if left >= right:
            return
        
        mid = (left + right) // 2
        self.mergeSort(arr, temp, res, left, mid)
        self.mergeSort(arr, temp, res, mid + 1, right)
        self.merger(arr, temp, res, left, right)
        
    def merger(self, arr, temp, res, left, right):
        mid = (left + right) // 2
        i, j, k = left, mid + 1, left
        
        while i <= mid and j <= right:
            if arr[i][0] <= arr[j][0]:
                res[arr[i][1]] += j - mid - 1
                temp[k] = arr[i]
                i += 1
            else:
                temp[k] = arr[j]
                j += 1
            k += 1
        
        while i <= mid:
            res[arr[i][1]] += j - mid - 1
            temp[k] = arr[i]
            i += 1
            k += 1
        while j <= right:
            temp[k] = arr[j]
            j += 1
            k += 1
            
        for k in range(left, right + 1):
            arr[k] = temp[k]