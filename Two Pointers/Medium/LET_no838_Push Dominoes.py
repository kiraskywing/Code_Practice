class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        dominoes = 'L' + dominoes + 'R'
        res = []
        
        left = 0
        for right in range(1, len(dominoes)):
            if dominoes[right] == '.':
                continue
            
            mid = right - left - 1
            if left > 0:
                res.append(dominoes[left])
            if dominoes[left] == dominoes[right]:
                res.append(dominoes[left] * mid)
            elif dominoes[left] == 'L' and dominoes[right] == 'R':
                res.append('.' * mid)
            else:
                res.append('R' * (mid // 2) + '.' * (mid % 2) + 'L' * (mid // 2))
            left = right
        
        return ''.join(res)