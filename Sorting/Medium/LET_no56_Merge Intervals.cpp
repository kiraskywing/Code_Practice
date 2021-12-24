class Solution {
public:
    vector<vector<int>> merge(vector<vector<int>>& intervals) {
        sort(intervals.begin(), intervals.end());
        vector<vector<int>> res;
        for (vector<int>& itv : intervals) {
            if (!res.empty() && itv[0] <= res.back()[1])
                res.back()[1] = max(res.back()[1], itv[1]);
            else
                res.push_back(itv);
        }
        return res;
    }
};