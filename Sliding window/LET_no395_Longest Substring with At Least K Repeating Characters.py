class Solution:
    # Solution 1: sliding window
    def longestSubstring(self, s: str, k: int) -> int:
        res = 0
        for numUniqueTarget in range(1, 27):
            arr = [0] * 26
            start = end = 0
            numUnique = numNoLessThanK = 0
            
            while end < len(s):
                if arr[ord(s[end]) - ord('a')] == 0: numUnique += 1
                arr[ord(s[end]) - ord('a')] += 1
                if arr[ord(s[end]) - ord('a')] == k: numNoLessThanK += 1
                end += 1
                
                while numUnique > numUniqueTarget:
                    if arr[ord(s[start]) - ord('a')] == k: numNoLessThanK -= 1
                    arr[ord(s[start]) - ord('a')] -= 1
                    if arr[ord(s[start]) - ord('a')] == 0: numUnique -= 1
                    start += 1
                
                if numUnique == numUniqueTarget and numUnique == numNoLessThanK:
                    res = max(end - start, res)
        
        return res
        
    # Solution 2: divide and conquer
    def longestSubstring(self, s: str, k: int) -> int:
        s_count = collections.Counter(s)
        for c in s_count:
            if s_count[c] < k:
                return max(self.longestSubstring(sub_s, k) for sub_s in s.split(c))
        return len(s)