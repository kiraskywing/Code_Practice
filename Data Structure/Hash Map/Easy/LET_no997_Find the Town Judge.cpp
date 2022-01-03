class Solution {
public:
    int findJudge(int n, vector<vector<int>>& trust) {
        vector<int> table(n + 1, 0);
        for (vector<int>& edge : trust) {
            table[edge[1]]++;
            table[edge[0]]--;
        }
        for (int i = 1; i <= n; i++)
            if (table[i] == n - 1)
                return i;
        return -1;
    }
};