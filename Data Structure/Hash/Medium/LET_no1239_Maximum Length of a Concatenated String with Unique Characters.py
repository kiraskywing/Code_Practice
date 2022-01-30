class Solution:
    def maxLength(self, arr: List[str]) -> int:
        dp = [set()]
        for a in arr:
            if len(set(a)) < len(a):
                continue
            a = set(a)
            for b in dp[:]:
                if a.intersection(b):
                    continue
                dp.append(a.union(b))
        return max(len(c) for c in dp)