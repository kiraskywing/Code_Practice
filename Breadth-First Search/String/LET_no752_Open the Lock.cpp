class Solution {
public:
    int openLock(vector<string>& deadends, string target) {
        unordered_set<string> memo(deadends.begin(), deadends.end());
        if (memo.count("0000"))
            return -1;

        int step = 0;
        queue<string> q;
        q.push("0000");

        while (!q.empty()) {
            int n = q.size();
            while (n-- > 0) {
                string cur = q.front();
                q.pop();
                cout << cur << endl;
                if (target.compare(cur) == 0)
                    return step;

                for (int i = 0; i < 4; i++) {
                    char c = cur[i];
                    cur[i] = (c - '0' + 1) % 10 + '0';
                    if (!memo.count(cur)) {
                        memo.insert(cur);
                        q.push(cur);
                    }

                    cur[i] = (c - '0' - 1 + 10) % 10 + '0';
                    if (!memo.count(cur)) {
                        memo.insert(cur);
                        q.push(cur);
                    }
                    cur[i] = c;
                }
            }

            step++;
        }

        return -1;
    }
};