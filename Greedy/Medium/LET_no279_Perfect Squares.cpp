class Solution {
public:
    int numSquares(int n) {
        vector<bool> visited(n + 1, false);
        vector<int> squares;
        queue<int> q;
        for (int i = 1; i * i <= n; i++) {
            int cur = i * i;
            squares.push_back(cur);
            visited[cur] = true;
            q.push(cur);
        }
        
        int res = 1;
        while (!q.empty()) {
            for (int i = q.size(); i > 0; i--) {
                int cur = q.front();
                q.pop();
                if (cur == n)
                    return res;
                
                for (int& num : squares) {
                    int nxt = cur + num;
                    if (nxt <= n && !visited[nxt]) {
                        visited[nxt] = true;
                        q.push(nxt);
                    }
                    else if (nxt > n)
                        break;
                }
            }
            res++;
        }
        return res;
    }
};