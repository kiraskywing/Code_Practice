class Solution {
private:
    int m, n, x_min, x_max, y_min, y_max;
public:
    int minArea(vector<vector<char>>& image, int x, int y) {
        m = image.size();
        n = image[0].size();
        if (m == 0 || n == 0)
            return 0;

        x_min = x_max = x;
        y_min = y_max = y;
        queue<pair<int,int>> q;
        q.push({x, y});
        unordered_set<int> visited;
        visited.insert(x * n + y);
        vector<pair<int,int>> shift = {{1, 0}, {0, 1}, {-1, 0}, {0, -1}};

        int x2, y2, key;
        while (!q.empty()) {
            int times = q.size();
            while (times-- > 0) {
                x = q.front().first;
                y = q.front().second;
                q.pop();

                for (auto& s : shift) {
                    x2 = x + s.first;
                    y2 = y + s.second;
                    if (0 <= x2 && x2 < m && 0 <= y2 && y2 < n && image[x2][y2] == '1') {
                        key = x2 * n + y2;
                        if (!visited.count(key)) {
                            visited.insert(key);
                            updateBoundary(x2, y2);
                            q.push({x2, y2});
                        }
                    }
                }
            }
        }

        return (x_max - x_min + 1) * (y_max - y_min + 1);
    }

    void updateBoundary(int x, int y) {
        x_min = min(x_min, x);
        x_max = max(x_max, x);
        y_min = min(y_min, y);
        y_max = max(y_max, y);
    }
};