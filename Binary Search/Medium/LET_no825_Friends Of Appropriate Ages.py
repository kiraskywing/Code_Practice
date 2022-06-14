class Solution:
    def numFriendRequests(self, ages: List[int]) -> int:
        ages.sort()
        res = 0
        for i in range(len(ages)):
            limit = ages[i] * 0.5 + 7
            upper = bisect.bisect_right(ages, ages[i])
            lower = bisect.bisect_right(ages, limit)
            res += max(upper - lower - 1, 0)
        return res

class Solution2:
    def numFriendRequests(self, ages: List[int]) -> int:
        memo = collections.Counter(ages)
        res = 0
        for x in memo:
            for y in memo:
                res += int(self.valid(x, y)) * memo[x] * (memo[y] - int(x == y))
        return res
        
    def valid(self, x, y):
        return not (y <= 0.5 * x + 7 or y > x or y > 100 and x < 100)

class Solution3:
    def numFriendRequests(self, ages: List[int]) -> int:
        age_count, pre_sum = [0] * 121, [0] * 121
        for age in ages:
            age_count[age] += 1
        for age in range(1, 121):
            pre_sum[age] = pre_sum[age - 1] + age_count[age]
            
        res = 0
        # y > 0.5 * x + 7 && y < x => 2x > x + 14 => x > 14 
        for age in range(15, 121):
            if age_count[age] == 0:
                continue
            count = pre_sum[age] - pre_sum[int(age * 0.5 + 7)]
            res += count * age_count[age] - age_count[age]
    
        return res