class Solution:
    def numTrees(self, n: int) -> int:
        # G(n): the number of unique BST for a sequence of length n.
        # F(i, n), 1 <= i <= n: the number of unique BST, where the number i is the root of BST, and the sequence ranges from 1 to n.
        # G(n) = F(1, n) + F(2, n) + ... + F(n, n).
        # length 1 (only a root) or 0 (empty tree): G(0)=1, G(1)=1.
        # F(i, n) = G(i-1) * G(n-i)	1 <= i <= n
        # G(n) = G(0) * G(n-1) + G(1) * G(n-2) + … + G(n-1) * G(0) 
        
        res = [0] * (n + 1)
        res[0] = res[1] = 1
        
        for i in range(2, n + 1):
            for j in range(i):
                res[i] += res[j] * res[i - j - 1]
        
        return res[n]