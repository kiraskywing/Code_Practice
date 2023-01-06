class Solution {
public:
    int maxIceCream(vector<int>& costs, int coins) {
        int max_cost = *max_element(costs.begin(), costs.end());
        int res = 0;

        vector<int> bucket(max_cost + 1);
        for (int cost : costs)
            bucket[cost]++;

        for (int cost = 1; cost <= max_cost; cost++) {
            if (coins < cost)
                break;
            
            int count = min(bucket[cost], coins / cost);
            coins -= cost * count;
            res += count;
        }

        return res;
    }
};

class Solution2 {
public:
    int maxIceCream(vector<int>& costs, int coins) {
        sort(costs.begin(), costs.end());
        int res = 0;
        for (int cur : costs) {
            if (cur <= coins) {
                coins -= cur;
                res++;
            }
            else
                return res;
        }

        return res;
    }
};