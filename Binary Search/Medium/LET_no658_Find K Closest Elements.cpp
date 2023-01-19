class Solution {
public:
    vector<int> findClosestElements(vector<int>& arr, int k, int x) {
        int upper_idx = getFirstUpper(arr, x);
        int lower_idx = upper_idx - 1;

        for (int i = 0; i < k; i++) {
            if (lowerIsChosen(arr, lower_idx, upper_idx, x))
                lower_idx--;
            else
                upper_idx++;
        }

        return {arr.begin() + lower_idx + 1, arr.begin() + upper_idx};
    }

    int getFirstUpper(vector<int>& arr, int target) {
        int left = 0, right = arr.size() - 1;
        while (left + 1 < right) {
            int mid = left + (right - left) / 2;
            if (arr[mid] >= target)
                right = mid;
            else
                left = mid;         
        }

        if (arr[left] >= target)
            return left;
        if (arr[right] >= target)
            return right;
        return arr.size();
    }

    bool lowerIsChosen(vector<int>& arr, int lower, int upper, int target) {
        if (lower < 0)
            return false;
        return upper == arr.size() || target - arr[lower] <= arr[upper] - target;
    }
};