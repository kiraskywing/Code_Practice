class Solution {
public:
    int findMin(vector<int>& nums) {
        int left = 0, right = nums.size() - 1;
        while (left + 1 < right) {
            int mid = left + (right - left) / 2;
            if (nums[mid] < nums[right])
                right = mid;
            else if (nums[mid] == nums[right])
                right--;
            else
                left = mid;
        }

        return nums[left] < nums[right] ? nums[left] : nums[right];
    }
};