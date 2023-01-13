class Solution {
public:
    int longestPath(vector<int>& parent, string s) {
        int n = parent.size();
        vector<vector<int>> children(n);
        for (int i = 1; i < n; i++)
            children[parent[i]].push_back(i);

        int res = 1;
        dfs(0, children, s, res);
        return res;
    }

    int dfs(int cur_node, vector<vector<int>>& children, string& s, int& res) {
        int longest = 0, second_long = 0;
        for (int child_node : children[cur_node]) {
            int child_longest = dfs(child_node, children, s, res);
            
            if (s[cur_node] == s[child_node])
                continue;
            
            if (child_longest > longest) {
                second_long = longest;
                longest = child_longest;
            }
            else if (child_longest > second_long)
                second_long = child_longest;
        }

        res = max(res, longest + second_long + 1);            
        return longest + 1;
    }
};