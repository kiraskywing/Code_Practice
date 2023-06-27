class Solution {
public:
    vector<vector<int>> kSmallestPairs(vector<int>& nums1, vector<int>& nums2, int k) {
        int m = nums1.size(), n = nums2.size();
        vector<vector<int>> res;
        if (m == 0 || n == 0)
            return res;

        typedef pair<int, pair<int,int>> item;
        priority_queue<item, vector<item>, greater<item>> pq;
        for (int i = 0; i < m; i++)
            pq.push({nums1[i] + nums2[0], {i, 0}});

        while (!pq.empty() && k-- > 0) {
            int val = pq.top().first;
            int i = pq.top().second.first, j = pq.top().second.second;
            pq.pop();

            vector<int> cur = {nums1[i], nums2[j]};
            res.push_back(cur);
            
            if (j + 1 == n)
                continue;
            
            j++;
            pq.push({nums1[i] + nums2[j], {i, j}});
        }

        return res;
    }
};