class Solution:
    def countAndSay(self, n: int) -> str:
        s = '1'
        for _ in range(n - 1):
            s2 = []
            left = 0
            m = len(s)
            
            while left < m:
                right = left
                while right < m and s[right] == s[left]:
                    right += 1
                s2.extend([str(right - left), s[left]])
                left = right
            
            s = ''.join(s2)
        
        return s