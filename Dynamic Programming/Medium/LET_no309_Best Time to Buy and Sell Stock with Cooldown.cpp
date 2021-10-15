class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int n = prices.size();
        if (n <= 1)
            return 0;
        
        vector<int> afterRest(n, 0), afterBuy(n, 0), afterSell(n, 0);
        afterRest[0] = 0;
        afterBuy[0] = -prices[0];
        afterSell[0] = INT_MIN;
        for (int i = 1; i < n; i++) {
            afterRest[i] = max(afterRest[i - 1], afterSell[i - 1]);
            afterBuy[i] = max(afterBuy[i - 1], afterRest[i - 1] - prices[i]);
            afterSell[i] = afterBuy[i - 1] + prices[i];
        }
        
        return max(afterRest[n - 1], afterSell[n - 1]);
    }
};