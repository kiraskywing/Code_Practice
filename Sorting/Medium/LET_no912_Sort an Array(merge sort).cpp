class Solution {
public:
    vector<int> sortArray(vector<int>& nums) {
        int n = nums.size();
        vector<int> temp(n, 0);
        helper(nums, temp, 0, n - 1);
        return nums;
    }

    void helper(vector<int>& nums, vector<int>& temp, int left, int right) {
        if (left >= right)
            return;

        int mid = (left + right) / 2;
        helper(nums, temp, left, mid);
        helper(nums, temp, mid + 1, right);
        merger(nums, temp, left, right);
    }

    void merger(vector<int>& nums, vector<int>& temp, int left, int right) {
        int mid = (left + right) / 2;
        int i = left, j = mid + 1, k = left;
        while (i <= mid && j <= right) {
            if (nums[i] < nums[j])
                temp[k++] = nums[i++];
            else
                temp[k++] = nums[j++];
        }

        while (i <= mid)
            temp[k++] = nums[i++];
        while (j <= right)
            temp[k++] = nums[j++];

        for (i = left; i <= right; i++)
            nums[i] = temp[i];
    }
};