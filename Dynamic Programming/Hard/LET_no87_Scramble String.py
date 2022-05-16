class Solution:
    def isScramble(self, s1: str, s2: str) -> bool:
        if len(s1) != len(s2):
            return False
        
        """
		Let F(i, j, k) = whether the substring S1[i..i + k - 1] is a scramble of S2[j..j + k - 1] or not
        Since each of these substrings is a potential node in the tree, we need to check for all possible cuts.
		Let q be the length of a cut (hence, q < k), then we are in the following situation:
		 
		S1 [   x1    |         x2         ]
		   i         i + q                i + k - 1
		
		here we have two possibilities:
		     
		S2 [   y1    |         y2         ]
		   j         j + q                j + k - 1
		   
		or 
		
		S2 [       y1        |     y2     ]
		   j                 j + k - q    j + k - 1
		
		which in terms of F means:
		
		F(i, j, k) = for some 1 <= q < k we have:
		(F(i, j, q) AND F(i + q, j + q, k - q)) OR (F(i, j + k - q, q) AND F(i + q, j, k - q))
		 
		Base case is k = 1, where we simply need to check for S1[i] and S2[j] to be equal 
		 """

        n = len(s1)
        dp = [[[False for _ in range(n + 1)] for _ in range(n)] for _ in range(n)]
        
        for k in range(1, n + 1):
            for i in range(n - k + 1):
                for j in range(n - k + 1):
                    if k == 1:
                        dp[i][j][k] = s1[i] == s2[j]
                    else:
                        for q in range(1, k):
                            if dp[i][j][q] and dp[i+q][j+q][k-q] or dp[i][j+k-q][q] and dp[i+q][j][k-q]:
                                dp[i][j][k] = True
                                break
        
        return dp[0][0][n]