class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        memo = collections.defaultdict(list)
        for s in strings:
            base = ord(s[0]) - ord('a')
            temp = []
            for c in s:
                num = (ord(c) - ord('a') - base + 26) % 26
                temp.append(num)
            memo[tuple(temp)].append(s)
        
        return [values for values in memo.values()]