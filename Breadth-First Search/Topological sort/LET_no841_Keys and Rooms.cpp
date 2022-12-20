class Solution {
public:
    bool canVisitAllRooms(vector<vector<int>>& rooms) {
        queue<int> q;
        unordered_set<int> visited;
        q.push(0);
        visited.insert(0);

        while (!q.empty()) {
            int n = q.size();
            for (int i = 0; i < n; i++) {
                int cur = q.front();
                q.pop();
                for (int nxt : rooms[cur]) {
                    if (!visited.count(nxt)) {
                        visited.insert(nxt);
                        q.push(nxt);
                    }
                }
            }
        }

        return rooms.size() == visited.size();
    }
};