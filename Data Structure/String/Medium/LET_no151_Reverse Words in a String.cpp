class Solution {
public:
    string reverseWords(string s) {
        reverse(s.begin(), s.end());
        int cur = 0;
        for (int i = 0; i < s.size(); i++) {
            if (s[i] != ' ') {
                if (cur != 0) 
                    s[cur++] = ' ';
                int j = i;
                while (j < s.size() && s[j] != ' ')
                    s[cur++] = s[j++];
                reverse(s.begin() + cur - (j - i), s.begin() + cur);
                i = j;
            }
        }
        return s.substr(0, cur);
    }
};