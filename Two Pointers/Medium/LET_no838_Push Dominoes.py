class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        dominoes = 'L' + dominoes + 'R'
        
        res = []
        left = 0
        for right in range(1, len(dominoes)):
            if dominoes[right] == '.':
                continue
                
            if left > 0:
                res.append(dominoes[left])
                
            mids = right - left - 1
            if dominoes[left] == dominoes[right]:
                res.append(dominoes[left] * mids)
            elif dominoes[left] == 'R' and dominoes[right] == 'L':
                res.append('R' * (mids // 2) + '.' * (mids % 2) + 'L' * (mids // 2))
            else:
                res.append('.' * mids)
            
            left = right
        
        return ''.join(res)