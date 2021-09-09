class Solution {
public:
    string shiftingLetters(string s, vector<int>& shifts) {
        int pre = 0, cur;
        for (int i = s.size() - 1; i >= 0; i--) {
            cur = (pre + shifts[i]) % 26;
            pre = cur;
            s[i] = 'a' + (s[i] - 'a' + cur) % 26;
        }
        return s;
    }
};