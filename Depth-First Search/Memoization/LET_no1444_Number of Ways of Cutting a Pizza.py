class Solution:
    def ways(self, pizza: List[str], k: int) -> int:
        m, n = len(pizza), len(pizza[0])
        self.mod = 10 ** 9 + 7
        
        pre_sum = [[0 for _ in range(n)] for _ in range(m)]
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                pre_sum[i][j] = pizza[i][j] == 'A'
                if i < m - 1: pre_sum[i][j] += pre_sum[i + 1][j]
                if j < n - 1: pre_sum[i][j] += pre_sum[i][j + 1]
                if i < m - 1 and j < n - 1: pre_sum[i][j] -= pre_sum[i + 1][j + 1]
                    
        return self.helper(pre_sum, k - 1, 0, 0, dict())
    
    def helper(self, pre_sum, cuts, start_i, start_j, memo):
        if pre_sum[start_i][start_j] == 0:
            return 0
        if cuts == 0:
            return 1
        
        if (cuts, start_i, start_j) not in memo:
            cur = 0
            
            for i in range(start_i + 1, len(pre_sum)):
                if pre_sum[start_i][start_j] - pre_sum[i][start_j] > 0:
                    cur += self.helper(pre_sum, cuts - 1, i, start_j, memo)
                    cur %= self.mod
            
            for j in range(start_j + 1, len(pre_sum[0])):
                if pre_sum[start_i][start_j] - pre_sum[start_i][j] > 0:
                    cur += self.helper(pre_sum, cuts - 1, start_i, j, memo)
                    cur %= self.mod
            
            memo[(cuts, start_i, start_j)] = cur
            
        return memo[(cuts, start_i, start_j)]