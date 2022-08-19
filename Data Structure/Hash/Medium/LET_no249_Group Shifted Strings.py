class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        memo = collections.defaultdict(list)
        for s in strings:
            temp = [(ord(c) + 26 - ord(s[0])) % 26 for c in s]
            memo[tuple(temp)].append(s)
        
        return [values for values in memo.values()]
            