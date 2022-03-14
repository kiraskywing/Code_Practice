class Solution:
    def numDecodings(self, s: str) -> int:
        mod = 10 ** 9 + 7
        pre, pre_is_1, pre_is_2 = 1, 0, 0
        for c in s:
            if c == '*':
                cur = pre * 9 + pre_is_1 * 9 + pre_is_2 * 6
                cur_is_1 = cur_is_2 = pre
            else:
                cur = (c > '0') * pre + pre_is_1 + (c <= '6') * pre_is_2
                cur_is_1 = (c == '1') * pre
                cur_is_2 = (c == '2') * pre
            
            pre, pre_is_1, pre_is_2 = cur % mod, cur_is_1, cur_is_2
        
        return pre