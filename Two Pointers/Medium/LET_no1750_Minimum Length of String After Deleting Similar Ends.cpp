class Solution {
public:
    int minimumLength(string s) {
        int i = 0, j = s.size() - 1;
        while (i < j && s[i] == s[j]) {
            char cur = s[i];
            while (i <= j && s[i] == cur)
                i++;
            while (i <= j && s[j] == cur)
                j--;
        }

        return i <= j ? j - i + 1 : 0;
    }
};