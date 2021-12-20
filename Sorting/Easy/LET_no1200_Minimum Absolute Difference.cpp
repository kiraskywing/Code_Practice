class Solution {
public:
    vector<vector<int>> minimumAbsDifference(vector<int>& arr) {
        sort(arr.begin(), arr.end());
        int diff = arr[1] - arr[0];
        vector<vector<int>> res = {{arr[0], arr[1]}};
        
        for (int i = 2; i < arr.size(); i++) {
            if (arr[i] - arr[i - 1] == diff)
                res.push_back({arr[i - 1], arr[i]});
            else if (arr[i] - arr[i - 1] < diff) {
                diff = arr[i] - arr[i - 1];
                res = {{arr[i - 1], arr[i]}};
            }
        }
        
        return res;
    }
};