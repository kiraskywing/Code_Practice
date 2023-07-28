class Solution {
private:
    int n;
public:
    vector<string> restoreIpAddresses(string s) {
        n = s.size();
        vector<string> res;
        string cur = "";
        dfs(s, 0, 0, cur, res);
        return res;
    }

    void dfs(string& s, int start, int count, string& cur, vector<string>& res) {
        if (count == 4) {
            if (start == n) {
                cur.pop_back();
                res.push_back(cur);
            }
            return;
        }

        for (int len = 1; len < 4; len++) {
            if (start + len > n)
                continue;
            string sub = s.substr(start, len);
            int value = stoi(sub);
            if (value <= 255) {
                cur += sub + ".";
                dfs(s, start + len, count + 1, cur, res);
                cur.resize(start + count);
            }

            if (s[start] == '0')
                break;
        }
    }
};