class Solution {
public:
    int findMinArrowShots(vector<vector<int>>& points) {
        if (points.size() == 0)
            return 0;
        
        sort(points.begin(), points.end(), [](vector<int>& a, vector<int>& b) { return a[1] < b[1]; });
        int res = 1, end = points[0][1];

        for (vector<int>& p : points) {
            int left = p[0], right = p[1];
            if (left > end) {
                res++;
                end = right;
            }
        }

        return res;
    }
};