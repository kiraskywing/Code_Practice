class Solution {
public:
    int minTime(int n, vector<vector<int>>& edges, vector<bool>& hasApple) {
        vector<vector<int>> memo(n);
        for (auto& e : edges) {
            memo[e[0]].push_back(e[1]);
            memo[e[1]].push_back(e[0]);
        }

        return dfs(0, -1, memo, hasApple);
    }

    int dfs(int cur, int parent, vector<vector<int>>& memo, vector<bool>& hasApple) {
        int cur_cost = 0, child_cost = 0;
        for (int child : memo[cur]) {
            if (child == parent)
                continue;

            child_cost = dfs(child, cur, memo, hasApple);
            if (child_cost > 0 || hasApple[child])
                cur_cost += child_cost + 2;
        }

        return cur_cost;
    }
};