class Solution:
    def countAndSay(self, n: int) -> str:
        res = ""
        for i in range(n):
            if i == 0:
                res = "1"
            else:
                temp = []
                count = 0
                cur = None
                for c in res:
                    if cur is None:
                        cur = c
                    if cur == c:
                        count += 1
                    else:
                        temp.append(str(count) + cur)
                        cur = c
                        count = 1      
                res = ''.join(temp) + str(count) + cur
                
        return res