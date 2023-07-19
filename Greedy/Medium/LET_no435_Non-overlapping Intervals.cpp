class Solution {
public:
    int eraseOverlapIntervals(vector<vector<int>>& intervals) {
        sort(intervals.begin(), intervals.end(), [](vector<int>& a, vector<int>& b){ return a[1] < b[1]; });
        int end = intervals[0][1], count = 1, n = intervals.size();

        for (int i = 1; i < n; i++) {
            if (end <= intervals[i][0]) {
                end = intervals[i][1];
                count++;
            }
        }

        return n - count;
    }
};