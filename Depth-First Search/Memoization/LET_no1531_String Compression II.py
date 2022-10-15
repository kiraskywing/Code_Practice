class Solution:
    def getLengthOfOptimalCompression(self, s: str, k: int) -> int:
        return self.helper(s, 0, "", 0, k, dict())
    
    def helper(self, s, start, prev_ch, prev_count, delete_left, memo):
        if delete_left < 0:
            return float('inf')
        if start == len(s):
            return 0
        
        if (start, prev_ch, prev_count, delete_left) not in memo:
            res = 0
            if s[start] == prev_ch:
                incr = 1 if prev_count in (1, 9, 99) else 0
                res = incr + self.helper(s, start + 1, prev_ch, prev_count + 1, delete_left, memo)
            else:
                keep_cur = 1 + self.helper(s, start + 1, s[start], 1, delete_left, memo)
                delete_cur = self.helper(s, start + 1, prev_ch, prev_count, delete_left - 1, memo)
                res = min(keep_cur, delete_cur)
            memo[(start, prev_ch, prev_count, delete_left)] = res
        
        return memo[(start, prev_ch, prev_count, delete_left)]