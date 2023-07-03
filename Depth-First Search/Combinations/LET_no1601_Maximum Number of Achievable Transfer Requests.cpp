class Solution {
private:
    int max_res;
public:
    int maximumRequests(int n, vector<vector<int>>& requests) {
        max_res = 0;
        vector<int> memo(n, 0);
        dfs(requests, memo, 0, 0);
        return max_res;
    }

    void dfs(vector<vector<int>>& requests, vector<int>& memo, int idx, int count) {
        if (idx == requests.size()) {
            for (int num : memo) {
                if (num != 0)
                    return;
            }
            
            max_res = max(max_res, count);
            return;
        }

        int from = requests[idx][0], to = requests[idx][1];
        memo[from]--;
        memo[to]++;
        dfs(requests, memo, idx + 1, count + 1);
        memo[to]--;
        memo[from]++;

        dfs(requests, memo, idx + 1, count);
    }
};