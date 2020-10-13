class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        result = []
        self.dfs(1, result, k, n, [])
        return result
            
    def dfs(self, idx, result, size, target, temp):
        if len(temp) == size and target == 0:
            result.append(temp[:])
            return

        for i in range(idx, 10):
            if i > target:
                break
            temp.append(i)
            self.dfs(i + 1, result, size, target - i, temp)
            temp.pop()
