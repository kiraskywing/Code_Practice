class Solution {
public:
    int findKthLargest(vector<int>& nums, int k) {
        return helper(nums, 0, nums.size() - 1, k - 1);
    }

    int helper(vector<int>& nums, int left, int right, int target) {
        if (left == right)
            return nums[left];
        
        int i = left, j = right;
        int pivot = nums[(i + j) / 2];

        while (i <= j) {
            while (i <= j && nums[i] > pivot) 
                i++;
            while (i <= j && nums[j] < pivot)
                j--;
            if (i <= j)
                swap(nums[i++], nums[j--]);
        }

        if (target <= j)
            return helper(nums, left, j, target);
        if (target >= i)
            return helper(nums, i, right, target);
        return nums[target];
    }
};