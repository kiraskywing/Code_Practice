class Solution {
public:
    int findMin(vector<int>& nums) {
        int left = 0, right = nums.size() - 1;
        int target = nums[right];
        
        while (left + 1 < right) {
            int mid = (left + right) / 2;
            if (nums[mid] <= target)
                right = mid;
            else
                left = mid;
        }
        
        return min(nums[left], nums[right]);
    }
};