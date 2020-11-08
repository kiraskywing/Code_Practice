class Solution:
    def maxProfit(self, inventory: List[int], orders: int) -> int:
        arr = sorted(collections.Counter(inventory).items(), reverse=True) + [(0, 0)]
        res = i = same_times = 0
        mod = 10 ** 9 + 7
        
        while orders > 0:
            same_times += arr[i][1]
            sell_times = min(orders, same_times * (arr[i][0] - arr[i + 1][0]))
            whole, residual = sell_times // same_times, sell_times % same_times
            res += (same_times * (whole * (arr[i][0] + (arr[i][0] - whole + 1))) // 2 + residual * (arr[i][0] - whole)) % mod
            orders -= sell_times
            i += 1
        
        return res % mod