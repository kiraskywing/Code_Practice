class Solution {
public:
    string removeStars(string s) {
        int i = 0;
        for (int j = 0; j < s.size(); j++) {
            if (s[j] == '*')
                i--;
            else 
                s[i++] = s[j];
        }

        return s.substr(0, i);
    }
};