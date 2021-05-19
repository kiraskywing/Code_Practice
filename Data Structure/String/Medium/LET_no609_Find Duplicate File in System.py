class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        records = collections.defaultdict(list)
        
        for path in paths:
            path = path.split(' ')
            root = path[0]
            for i in range(1, len(path)):
                fileName, _, content = path[i].partition('(')
                records[content[:-1]].append(root + '/' + fileName)
        
        return [path for path in records.values() if len(path) >= 2]    