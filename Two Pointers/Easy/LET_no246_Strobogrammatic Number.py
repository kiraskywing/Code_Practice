class Solution:
    def isStrobogrammatic(self, num: str) -> bool:
        memo = {'6':'9', '9':'6', '0':'0', '1':'1', '8':'8'}
        i, j = 0, len(num) - 1
        while i <= j and num[i] in memo and memo[num[i]] == num[j]:
            i += 1
            j -= 1
        return i > j