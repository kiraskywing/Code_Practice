class Solution {
public:
    vector<int> searchRange(vector<int>& nums, int target) {
        if (nums.empty())
            return {-1, -1};
        
        return {findFirst(nums, target), findLast(nums, target)};
    }

    int findFirst(vector<int>& nums, int target) {
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

    int findLast(vector<int>& nums, int target) {
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