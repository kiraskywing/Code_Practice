class Solution {
public:
    int assignBikes(vector<vector<int>>& workers, vector<vector<int>>& bikes) {
        vector<int> memo(1 << bikes.size(), INT_MIN);
        return dfs(0, workers, bikes, 0, memo);
    }

    int dfs(int i, vector<vector<int>>& workers, vector<vector<int>>& bikes, int used_bikes, vector<int>& memo) {
        if (i == workers.size())
            return 0;

        if (memo[used_bikes] == INT_MIN) {
            int cur = INT_MAX;
            for (int j = 0; j < bikes.size(); j++) {
                if (used_bikes & (1 << j))
                    continue;
                cur = min(cur, getDist(workers[i], bikes[j]) + dfs(i + 1, workers, bikes, used_bikes | (1 << j), memo));
            }
            memo[used_bikes] = cur;
        }

        return memo[used_bikes];
    }

    int getDist(vector<int>& a, vector<int>& b) {
        return abs(a[0] - b[0]) + abs(a[1] - b[1]);
    }
};