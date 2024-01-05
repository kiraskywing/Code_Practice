class Solution {
public:
    int lengthOfLIS(vector<int>& nums) {
        int n = nums.size();
        vector<int> sequence(n + 1, INT_MAX);
        sequence[0] = INT_MIN;

        for (int num : nums) {
            int i = getPos(sequence, num);
            sequence[i] = num;
        }

        for (int i = n; i > 0; i--) {
            if (sequence[i] != INT_MAX)
                return i;
        }

        return 0;
    }

    int getPos(vector<int>& arr, int target) {
        int left = 0, right = arr.size() - 1;
        while (left + 1 < right) {
            int mid = left + (right - left) / 2;
            if (arr[mid] < target)
                left = mid;
            else
                right = mid;
        }

        if (arr[right] >= target)
            return right;
        return left;
    }
};