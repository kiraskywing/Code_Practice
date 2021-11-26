class Solution {
public:
    int searchInsert(vector<int>& nums, int target) {
        int i = 0, j = nums.size() - 1;
        while (i + 1 < j) {
            int mid = (i + j) / 2;
            if (nums[mid] < target)
                i = mid;
            else
                j = mid;
        }
        
        if (nums[i] >= target)
            return i;
        else if (nums[j] >= target)
            return j;
        return j + 1;
    }
};