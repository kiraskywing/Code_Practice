class Solution {
public:
    int triangleNumber(vector<int>& nums) {
        int n = nums.size();
        if (n < 3)
            return 0;
        
        sort(nums.begin(), nums.end());
        
        int res = 0;
        for (int i = 2; i < n; i++) {
            int left = 0, right = i - 1;
            while (left < right) {
                if (nums[left] + nums[right] > nums[i]) {
                    res += right - left;
                    right--;
                }
                else
                    left++;
            }
        }

        return res;
    }
};