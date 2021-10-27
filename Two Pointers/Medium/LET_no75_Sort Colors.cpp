class Solution {
public:
    void sortColors(vector<int>& nums) {
        int i = helper(nums, 0, 0);
        helper(nums, i, 1);
    }
    int helper(vector<int>& nums, int i, int pivot) {
        int left = i, right = nums.size() - 1;
        while (left <= right) {
            while (left <= right && nums[left] == pivot)
                left++;
            while (left <= right && nums[right] != pivot)
                right--;
            if (left <= right) 
                swap(nums[left++], nums[right--]);
        }
        return left;
    }
};