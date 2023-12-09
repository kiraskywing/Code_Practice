class Solution {
public:
    bool wordPatternMatch(string pattern, string s) {
        unordered_map<char, string> ch2words;
        unordered_set<string> used_words;
        return helper(pattern, 0, s, 0, ch2words, used_words);
    }

    bool helper(string& pattern, int i, string& s, int j, unordered_map<char, string>& ch2words, unordered_set<string>& used_words) {
        if (i == pattern.size())
            return j == s.size();

        char c = pattern[i];
        auto it = ch2words.find(c);
        if (it != ch2words.end()) {
            string str = it->second;
            string::size_type n = s.find(str, j);
            if (n == string::npos)
                return false;
            return helper(pattern, i + 1, s, j + str.size(), ch2words, used_words);
        }

        int n = s.size();
        for (int len = 1; len <= n - j; len++) {
            string str = s.substr(j, len);
            if (!used_words.count(str)) {
                ch2words[c] = str;
                used_words.insert(str);
                if (helper(pattern, i + 1, s, j + len, ch2words, used_words))
                    return true;
                used_words.erase(str);
                ch2words.erase(c);
            }
        }

        return false;
    }
};