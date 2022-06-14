class Solution:
    def findRLEArray(self, encoded1: List[List[int]], encoded2: List[List[int]]) -> List[List[int]]:
        res = []
        m, n = len(encoded1), len(encoded2)
        i = j = 0
        while i < m and j < n:
            count1, count2 = encoded1[i][1], encoded2[j][1]
            cur_count = min(count1, count2)
            val = encoded1[i][0] * encoded2[j][0]
            
            if not res or val != res[-1][0]:
                res.append([val, cur_count])
            else:
                res[-1][1] += cur_count
            
            encoded1[i][1] -= cur_count
            if encoded1[i][1] == 0:
                i += 1
            encoded2[j][1] -= cur_count
            if encoded2[j][1] == 0:
                j += 1
        
        return res