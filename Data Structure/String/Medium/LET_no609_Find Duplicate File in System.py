class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        memo = collections.defaultdict(list)
        for p in paths:
            p = p.split()
            folder = p[0]
            for i in range(1, len(p)):
                file, content = p[i].split('(')
                memo[content[:-1]].append(folder + '/' + file)
                
        return [values for values in memo.values() if len(values) > 1]