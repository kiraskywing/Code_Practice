# The same as Lintcode no.575_Decode String

class Solution:
    def decodeString(self, s: str) -> str:
        stack, num, cur_str = [], 0, ''
        
        for ch in s:
            if ch == '[':
                stack.append([cur_str, num])
                cur_str = ''
                num = 0
            elif ch == ']':
                pre_str, pre_num = stack.pop()
                cur_str = pre_str + pre_num * cur_str
            elif ch.isdigit():
                num = num * 10 + int(ch)
            else:
                cur_str += ch
        
        return cur_str