class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
        res = []
        self.dfs(num, res, "", 0, None, target)
        return res
    
    def dfs(self, num, res, path, value, prev, target):
        if not num:
            if value == target:
                res.append(path)
            return
        
        for i in range(1, len(num) + 1):
            temp = int(num[:i])
            if i == 1 or i > 1 and num[0] != '0':
                if prev is None:
                    self.dfs(num[i:], res, num[:i], temp, temp, target)
                else:
                    self.dfs(num[i:], res, path + '+' + num[:i], value + temp, temp, target)
                    self.dfs(num[i:], res, path + '-' + num[:i], value - temp, -temp, target)
                    self.dfs(num[i:], res, path + '*' + num[:i], value - prev + prev * temp, prev * temp, target)