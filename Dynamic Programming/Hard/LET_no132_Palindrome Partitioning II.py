class Solution:
    """
    @param s: A string
    @return: An integer
    """

    def minCut(self, s):
        if not s:
            return 0
        
        n = len(s)
        is_palindrome = self.getPalindrome(s, n)
        cuts = [i - 1 for i in range(n + 1)]
        
        for length in range(1, n + 1):
            for left in range(length):
                right = length - 1
                if is_palindrome[left][right]:
                    cuts[length] = min(cuts[length], cuts[left] + 1)
        
        return cuts[n]
    
    def getPalindrome(self, s, n):
        dp = [[False] * n for _ in range(n)]
        
        for length in range(n):
            for left in range(n - length):
                right = left + length
                dp[left][right] = s[left] == s[right] and (right - left < 2 or dp[left + 1][right - 1])
                
        return dp
