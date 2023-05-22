// priority queue
class Solution1 {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        unordered_map<int, int> memo;
        for (int num : nums)
            memo[num]++;

        priority_queue<pair<int, int>> pq;
        for (auto it = memo.begin(); it != memo.end(); it++) {
            pq.push({-it->second, it->first});
            if (pq.size() > k)
                pq.pop();
        }

        vector<int> res;
        while (!pq.empty()) {
            res.push_back(pq.top().second);
            pq.pop();
        }

        return res;
    }
};

// bucket sort
class Solution2 {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        unordered_map<int, int> memo;
        for (int num : nums)
            memo[num]++;

        int n = nums.size();
        vector<vector<int>> bucket(n + 1, vector<int>());
        for (auto it = memo.begin(); it != memo.end(); it++)
            bucket[it->second].push_back(it->first);

        vector<int> res;
        int i = n;
        while (k > 0) {
            while (bucket[i].empty())
                i--;
            for (int j = 0; j < bucket[i].size() && k > 0; j++, k--)
                res.push_back(bucket[i][j]);
            i--;
        }

        return res;
    }
};

