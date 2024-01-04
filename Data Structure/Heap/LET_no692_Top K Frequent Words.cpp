class Solution {
public:
    vector<string> topKFrequent(vector<string>& words, int k) {
        unordered_map<string, int> memo;
        for (string& w : words)
            memo[w]++;
        
        auto cmp = [](pair<string, int>& a, pair<string, int>& b) { 
            if (a.second == b.second)
                return a.first.compare(b.first) < 0;
            return a.second > b.second;
        };
        priority_queue<pair<string, int>, vector<pair<string, int>>, decltype(cmp)> pq(cmp);
        for (auto it = memo.begin(); it != memo.end(); it++) {
            pq.push({it->first, it->second});
            if (pq.size() > k)
                pq.pop();
        }

        vector<string> res;
        while (!pq.empty()) {
            auto item = pq.top();
            pq.pop();
            res.push_back(item.first);
        }

        reverse(res.begin(), res.end());
        return res;
    }
};