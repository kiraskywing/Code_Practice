class Solution {
public:
    double findMedianSortedArrays(vector<int>& nums1, vector<int>& nums2) {
        int m = nums1.size(), n = nums2.size();
        if ((m + n) % 2 != 0)
            return findKth(nums1, nums2, (m + n) / 2 + 1) * 1.0;
        else {
            int first = findKth(nums1, nums2, (m + n) / 2);
            int second = findKth(nums1, nums2, (m + n) / 2 + 1);
            return (first + second) * 1.0 / 2;
        }
    }

    int findKth(vector<int>& nums1, vector<int>& nums2, int k) {
        int min_val = 0, max_val = 0;
        if (!nums1.empty()) {
            min_val = min(min_val, getMin(nums1));
            max_val = max(max_val, getMax(nums1));
        }
        if (!nums2.empty()) {
            min_val = min(min_val, getMin(nums2));
            max_val = max(max_val, getMax(nums2));
        }

        while (min_val + 1 < max_val) {
            int mid_val = min_val + (max_val - min_val) / 2;
            int count = countLessEqualTarget(nums1, mid_val) + countLessEqualTarget(nums2, mid_val);
            if (count >= k)
                max_val = mid_val;
            else
                min_val = mid_val;
        }

        int count = countLessEqualTarget(nums1, max_val) + countLessEqualTarget(nums2, max_val);
        if (count >= k)
            return max_val;
        return min_val;
    }

    int getMax(vector<int>& nums) {
        int res = INT_MIN;
        for (int num : nums)
            res = max(res, num);
        return res;
    }

    int getMin(vector<int>& nums) {
        int res = INT_MAX;
        for (int num : nums)
            res = min(res, num);
        return res;
    }

    int countLessEqualTarget(vector<int>& nums, int target) {
        if (nums.empty())
            return 0;

        int left = 0, right = nums.size() - 1;
        while (left + 1 < right) {
            int mid = left + (right - left) / 2;
            if (nums[mid] <= target)
                left = mid;
            else
                right = mid;
        }

        if (nums[right] <= target)
            return right + 1;
        if (nums[left] <= target)
            return left + 1;
        return 0;
    }
};