class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        len1, len2, len3 = len(s1), len(s2), len(s3)
        if len1 + len2 != len3:
            return False
        
        queue = collections.deque([(0, 0)])
        visited = set((0, 0))
        while queue:
            i, j = queue.popleft()
            if i + j == len3:
                return True
            if i + 1 <= len1 and s1[i] == s3[i + j] and (i + 1, j) not in visited:
                queue.append((i + 1, j))
                visited.add((i + 1, j))
            if j + 1 <= len2 and s2[j] == s3[i + j] and (i, j + 1) not in visited:
                queue.append((i, j + 1))
                visited.add((i, j + 1))
        
        return False