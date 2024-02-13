class Solution {
public:
    string firstPalindrome(vector<string>& words) {
        for (string& s : words) {
            if (isPalindrome(s))
                return s;
        }

        return "";
    }

    bool isPalindrome(string& s) {
        int i = 0, j = s.size() - 1;
        while (i < j && s[i] == s[j]) {
            i++;
            j--;
        }

        return i >= j;
    }
};