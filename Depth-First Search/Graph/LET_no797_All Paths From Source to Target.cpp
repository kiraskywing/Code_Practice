class Solution {
public:
    vector<vector<int>> allPathsSourceTarget(vector<vector<int>>& graph) {
        vector<vector<int>> res;
        vector<int> temp = {0};
        dfs(res, temp, 0, graph);
        return res;
    }
    
    void dfs(vector<vector<int>>& res, vector<int>& temp, int start, vector<vector<int>>& graph) {
        if (start == graph.size() - 1) {
            res.push_back(temp);
            return;
        }
        
        for (int i : graph[start]) {
            temp.push_back(i);
            dfs(res, temp, i, graph);
            temp.pop_back();
        }
    }
};