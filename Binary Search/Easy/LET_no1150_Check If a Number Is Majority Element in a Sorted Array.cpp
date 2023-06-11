class Solution {
public:
    bool isMajorityElement(vector<int>& nums, int target) {
        int lower_id = findLower(nums, target);
        int upper_id = findUpper(nums, target);
        if (lower_id == -1)
            return false;
        return upper_id - lower_id + 1 > nums.size() / 2;
    }

    int findLower(vector<int>& nums, int target) {
        int left = 0, right = nums.size() - 1;
        while (left + 1 < right) {
            int mid = left + (right - left) / 2;
            if (nums[mid] >= target)
                right = mid;
            else
                left = mid;
        }

        if (nums[left] == target)
            return left;
        if (nums[right] == target)
            return right;
        return -1;
    }

    int findUpper(vector<int>& nums, int target) {
        int left = 0, right = nums.size() - 1;
        while (left + 1 < right) {
            int mid = left + (right - left) / 2;
            if (nums[mid] <= target)
                left = mid;
            else
                right = mid;
        }

        if (nums[right] == target)
            return right;
        if (nums[left] == target)
            return left;
        return -1;
    }
};