class Solution:
    def kthSmallestPath(self, destination: List[int], k: int) -> str:
        r, c = destination
        res = []
        remDown = r
        
        for i in range(r + c):
            remSteps = r + c - (i + 1)
            com = math.comb(remSteps, remDown)
            if com >= k:
                res.append("H")
            else:
                k -= com
                remDown -= 1
                res.append("V")
        
        return ''.join(res)