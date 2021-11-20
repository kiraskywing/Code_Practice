class Solution {
public:
    int singleNonDuplicate(vector<int>& nums) {
        int left = 0, right = nums.size() - 1;
        while (left + 1 < right) {
            int mid = (left + right) / 2;
            if (mid % 2 == 0 && nums[mid] == nums[mid + 1] || mid % 2 && nums[mid] == nums[mid - 1])
                left = mid;
            else
                right = mid;
        }
        
        if (left % 2 == 0)
            return nums[left];
        return nums[right];
    }
};