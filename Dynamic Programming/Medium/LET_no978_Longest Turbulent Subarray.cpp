class Solution {
public:
    int maxTurbulenceSize(vector<int>& arr) {
        int res = 0;
        for (int i = 0, count = 0; i + 1 < arr.size(); i++, count *= -1) {
            if (arr[i] > arr[i + 1])
                count = count > 0 ? count + 1 : 1;
            else if (arr[i] < arr[i + 1])
                count = count < 0 ? count - 1 : -1;
            else
                count = 0;
            res = max(res, abs(count));
        }
        return res + 1;
    }
};