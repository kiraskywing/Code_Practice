class Solution {
public:
    int nthUglyNumber(int n) {
        unordered_set<long> memo = {1};
        priority_queue<long, vector<long>, greater<long>> pq;
        pq.push(1);

        long res, num;
        vector<long> factors = {2, 3, 5};
        while (n-- > 0) {
            res = pq.top();
            pq.pop();
            for (long f : factors) {
                num = res * f;
                if (!memo.count(num)) {
                    memo.insert(num);
                    pq.push(num);
                }
            }
        }

        return res;
    }
};