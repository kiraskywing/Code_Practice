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

class Solution2:
    def addOperators(self, num: str, target: int) -> List[str]:
        res = []
        self.dfs(num, 0, target, 0, None, [], res)
        return res
    
    def dfs(self, num, start, target, cur, prev, temp, res):
        if start == len(num):
            if cur == target:
                res.append(''.join(temp))
                return
            
        for i in range(start + 1, len(num) + 1):
            val = int(num[start:i])
            if i == start + 1 or i > start + 1 and num[start] != '0':
                if prev is None:
                    temp.append(str(val))
                    self.dfs(num, i, target, val, val, temp, res)
                    temp.pop()
                else:
                    temp.append('+' + str(val))
                    self.dfs(num, i, target, cur + val, val, temp, res)
                    temp.pop()
                    
                    temp.append('-' + str(val))
                    self.dfs(num, i, target, cur - val, -val, temp, res)
                    temp.pop()
                    
                    temp.append('*' + str(val))
                    self.dfs(num, i, target, cur - prev + prev * val, prev * val, temp, res)
                    temp.pop()