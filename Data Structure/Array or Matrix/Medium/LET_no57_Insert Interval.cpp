class Solution {
public:
    vector<vector<int>> insert(vector<vector<int>>& intervals, vector<int>& newInterval) {
        int n = intervals.size(), i = 0;
        bool used = false;
        vector<vector<int>> res;

        while (i < n or !used) {
            if (used || i < n && intervals[i][0] < newInterval[0]) {
                updateRes(res, intervals[i][0], intervals[i][1]);
                i++;
            }
            else {
                updateRes(res, newInterval[0], newInterval[1]);
                used = true;
            }
        }

        return res;
    }

    void updateRes(vector<vector<int>>& res, int start, int end) {
        if (res.empty() || start > res.back()[1])
            res.push_back({start, end});
        else
            res.back()[1] = max(res.back()[1], end);
    }
};