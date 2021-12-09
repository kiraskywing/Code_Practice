class Solution {
public:
    bool canReach(vector<int>& arr, int start) {
        queue<int> q;
        q.push(start);
        vector<int> c = {-1, 1};
        while (!q.empty()) {
            int cur = q.front();
            q.pop();
            if (arr[cur] == 0)
                return true;
            for (int i : c) {
                int nxt = cur + i * arr[cur];
                if (nxt < 0 || nxt >= arr.size() || arr[nxt] < 0)
                    continue;
                arr[nxt] = -arr[nxt];
                q.push(nxt);
            }
        }
        return false;
    }
};