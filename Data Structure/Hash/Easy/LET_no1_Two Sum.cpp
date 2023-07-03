class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> memo;
        for (int i = 0; i < nums.size(); i++) {
            int aim = target - nums[i];
            if (memo.count(aim))
                return {memo[aim], i};
            memo[nums[i]] = i;
        }

        return {};
    }
};