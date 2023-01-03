class Solution {
public:
    bool wordPattern(string pattern, string s) {
        stringstream ss;
        ss << s;
        string cur;
        vector<string> words;

        while (ss >> cur)
            words.push_back(cur);

        if (words.size() != pattern.size())
            return false;

        unordered_map<char, string> ch_to_word;
        unordered_set<string> used_words;

        for (int i = 0; i < pattern.size(); i++) {
            char c = pattern[i];
            string cur = words[i];

            auto it1 = ch_to_word.find(c);
            auto it2 = used_words.find(cur);
            if (it1 != ch_to_word.end() && it1->second != cur || it1 == ch_to_word.end() && it2 != used_words.end())
                return false;

            ch_to_word[c] = cur;
            used_words.insert(cur);
        }

        return true;
    }
};