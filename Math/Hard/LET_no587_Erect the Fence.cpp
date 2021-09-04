class Solution {
public:
    vector<vector<int>> outerTrees(vector<vector<int>>& trees) {
        int n = trees.size();
        sort(trees.begin(), trees.end(), [](vector<int>& a, vector<int>& b) { return a[0] < b[0] || a[0] == b[0] && a[1] < b[1]; });
        
        vector<vector<int>> res;
        for (int i = 0; i < n; i++) {
            while (res.size() > 1 && orientation(res[res.size() - 2], res[res.size() - 1], trees[i]) < 0)
                res.pop_back();
            res.push_back(trees[i]);
        }
        
        if (res.size() == n)
            return res;
        
        for (int i = n - 2; i >= 0; i--) {
            while (res.size() > 1 && orientation(res[res.size() - 2], res[res.size() - 1], trees[i]) < 0)
                res.pop_back();
            res.push_back(trees[i]);
        }
        res.pop_back();
        
        return res;
    }
    
    int orientation(vector<int>& o, vector<int>& a, vector<int>& b) {
        return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0]);
    }
};