class Solution:
    def similarRGB(self, color: str) -> str:
        candidates = ["00", "11", "22", "33", "44", "55", "66", "77", "88", "99",
                      "aa", "bb", "cc", "dd", "ee", "ff"]
        
        res = ['#']
        for i in range(1, len(color), 2):
            res.append(min(candidates, key=lambda x: abs(int(x, 16) - int(color[i:i+2], 16))))
        
        return ''.join(res)