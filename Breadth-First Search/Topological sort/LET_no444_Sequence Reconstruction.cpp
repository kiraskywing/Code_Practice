class Solution {
public:
    bool sequenceReconstruction(vector<int>& nums, vector<vector<int>>& sequences) {
        int n = nums.size();
        vector<int> indegree(n, 0);
        unordered_map<int, vector<int>> next_hop;

        for (vector<int>& seq : sequences) {
            for (int i = 1; i < seq.size(); i++) {
                int from = seq[i - 1] - 1, to = seq[i] - 1;
                indegree[to]++;
                next_hop[from].push_back(to);
            }
        }

        queue<int> q;
        for (int i = 0; i < n; i++) {
            if (indegree[i] == 0)
                q.push(i);
        }

        int idx = 0;
        while (!q.empty()) {
            if (q.size() > 1)
                return false;

            int cur = q.front();
            q.pop();
            if (cur != nums[idx] - 1)
                return false;
            idx++;

            for (int nxt : next_hop[cur]) {
                if (--indegree[nxt] == 0)
                    q.push(nxt);
            }
        }

        return true;
    }
};