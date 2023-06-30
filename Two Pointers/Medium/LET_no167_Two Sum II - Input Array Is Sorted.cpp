class Solution {
public:
    vector<int> twoSum(vector<int>& numbers, int target) {
        int left = 0, right = numbers.size() - 1;
        while (left < right) {
            int cur = numbers[left] + numbers[right];
            if (cur < target)
                left++;
            else if (cur > target)
                right--;
            else
                return {left + 1, right + 1};
        }

        return {};
    }
};