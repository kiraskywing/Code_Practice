class Solution {
public:
    int findSpecialInteger(vector<int>& arr) {
        int n = arr.size();
        int bar = int(ceil(n * 1.0 / 4));
        int left = 0, right, length = -1, candidate = -1;
        for (right = 1; right < n; right++) {
            if (arr[right] != arr[right - 1]) {
                if (right - left > length) {
                    length = right - left;
                    candidate = arr[left];
                }
                left = right;
            }
        }

        if (right - left > length)
            candidate = arr[left];

        return candidate;
    }
};