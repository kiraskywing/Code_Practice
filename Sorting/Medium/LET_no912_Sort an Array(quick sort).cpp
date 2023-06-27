class Solution {
public:
    vector<int> sortArray(vector<int>& nums) {
        partition(nums, 0, nums.size() - 1);
        return nums;
    }

    void partition(vector<int>& nums, int left, int right) {
        if (left >= right)
            return;

        int i = left, j = right;
        int pivot = nums[(i + j) / 2];

        while (i <= j) {
            while (i <= j && nums[i] < pivot)
                i++;
            while (i <= j && nums[j] > pivot)
                j--;

            if (i <= j)
                swap(nums[i++], nums[j--]);
        }

        partition(nums, left, j);
        partition(nums, i, right);
    }
};