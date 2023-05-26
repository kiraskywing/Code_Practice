class Solution {
public:
    int stoneGameII(vector<int>& piles) {
        int n = piles.size();
        if (n == 1)
            return piles[0];
            
        vector<int> pre_sum = vector<int>(n, 0);
        pre_sum[n - 1] = piles[n - 1];
        for (int i = n - 2; i >= 0; i--)
            pre_sum[i] = pre_sum[i + 1] + piles[i];

        vector<vector<int>> memo(n, vector<int>(n, 0));
        helper(piles, memo, pre_sum, 0, 1);

        return memo[0][1];
    }

    int helper(vector<int>& piles, vector<vector<int>>& memo, vector<int>& pre_sum, int i, int M) {
        if (i == piles.size())
            return 0;

        if (2 * M >= piles.size() - i)
            return pre_sum[i];

        if (memo[i][M] == 0) {
            int val = INT_MAX;
            for (int j = 1; j <= M * 2; j++)
                val = std::min(val, helper(piles, memo, pre_sum, i + j, std::max(j, M)));

            memo[i][M] = pre_sum[i] - val;
        }
        
        return memo[i][M];
    }
};