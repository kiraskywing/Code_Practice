class Solution {
public:
    int minimumDeviation(vector<int>& nums) {
        int res = INT_MAX, min_val = INT_MAX, cur;
        priority_queue<int> pq;
        for (int num : nums) {
            if (num % 2)
                num *= 2;
            pq.push(num);
            min_val = min(min_val, num);
        }
        while (pq.top() % 2 == 0) {
            cur = pq.top();
            res = min(res, cur - min_val);
            min_val = min(min_val, cur / 2);
            pq.push(cur / 2);
            pq.pop();
        }

        return min(res, pq.top() - min_val);        
    }
};