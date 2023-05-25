class Solution {
public:
    long long maxScore(vector<int>& nums1, vector<int>& nums2, int k) {
        int n = nums1.size();
        vector<pair<int, int>> items;
        for (int i = 0; i < n; i++)
            items.push_back({nums2[i], nums1[i]});
        sort(items.rbegin(), items.rend());

        priority_queue<int, vector<int>, greater<int>> pq;
        long long total = 0, res = 0;
        for (auto& [a, b] : items) {
            pq.push(b);
            total += b;
            if (pq.size() > k) {
                total -= pq.top();
                pq.pop();
            }
            if (pq.size() == k)
                res = max(res, total * a);
        }

        return res;
    }
};