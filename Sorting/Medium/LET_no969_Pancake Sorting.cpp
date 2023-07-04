class Solution {
public:
    vector<int> pancakeSort(vector<int>& arr) {
        vector<int> res;
        int num, idx, n = arr.size();
        for (num = n; num > 0; num--) {
            for (idx = 0; arr[idx] != num; idx++);
            
            reverse(arr.begin(), arr.begin() + idx + 1);
            res.push_back(idx + 1);
            reverse(arr.begin(), arr.begin() + num);
            res.push_back(num);
        }

        return res;
    }
};