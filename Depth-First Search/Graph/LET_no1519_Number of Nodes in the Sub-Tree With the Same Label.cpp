class Solution {
public:
    vector<int> countSubTrees(int n, vector<vector<int>>& edges, string labels) {
        vector<vector<int>> tree(n);
        for (auto& e : edges) {
            tree[e[0]].push_back(e[1]);
            tree[e[1]].push_back(e[0]);
        }

        vector<int> res(n, 0);
        dfs(0, -1, tree, labels, res);
        return res;
    }

    vector<int> dfs(int cur, int parent, vector<vector<int>>& tree, string& labels, vector<int>& res) {
        vector<int> ch_count(26);
        ch_count[labels[cur] - 'a'] = 1;
        
        for (int child : tree[cur]) {
            if (child == parent)
                continue;
            vector<int> child_count = dfs(child, cur, tree, labels, res);
            for (int i = 0; i < 26; i++)
                ch_count[i] += child_count[i];
        }
        
        res[cur] = ch_count[labels[cur] - 'a'];
        return ch_count;
    }
};