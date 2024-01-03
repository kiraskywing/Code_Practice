class Solution {
public:
    int numberOfBeams(vector<string>& bank) {
        vector<int> counts;
        for (string& s : bank) {
            int cnt = 0;
            for (char c : s)
                cnt += c == '1';
            if (cnt > 0)
                counts.push_back(cnt);
        }

        int res = 0;
        for (int i = 1; i < counts.size(); i++)
            res += counts[i] * counts[i - 1];

        return res;
    }
};