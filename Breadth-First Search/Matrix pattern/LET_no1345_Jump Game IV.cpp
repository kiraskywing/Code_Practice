class Solution {
public:
    int minJumps(vector<int>& arr) {
        int n = arr.size();
        unordered_map<int, vector<int>> idx2val;
        for (int i = 0; i < n; i++)
            idx2val[arr[i]].push_back(i);
        
        vector<bool> visited(n, false);
        visited[0] = true;
        queue<int> q; q.push(0);
        int steps = 0;
        
        while (!q.empty()) {
            for (int i = q.size(); i > 0; i--) {
                int cur = q.front(); q.pop();
                if (cur == n - 1)
                    return steps;
                
                vector<int>& next = idx2val[arr[cur]];
                next.push_back(cur - 1);
                next.push_back(cur + 1);
                for (int i : next) {
                    if (0 <= i && i < n && !visited[i]) {
                        visited[i] = true;
                        q.push(i);
                    }
                }
                next.clear();
            }
            steps++;
        }
        
        return 0;
    }
};