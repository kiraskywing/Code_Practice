class Solution:
    def unhappyFriends(self, n: int, preferences: List[List[int]], pairs: List[List[int]]) -> int:
        record = {}
        
        for i, j in pairs:
            record[i] = preferences[i][:preferences[i].index(j)]
            record[j] = preferences[j][:preferences[j].index(i)]
        
        ans = 0
            
        for i in record:
            for j in record[i]:
                if i in record[j]:
                    ans += 1
                    break
        
        return ans