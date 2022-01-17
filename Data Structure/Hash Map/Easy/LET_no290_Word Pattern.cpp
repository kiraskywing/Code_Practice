class Solution {
public:
    bool wordPattern(string pattern, string s) {
        stringstream ss;
        ss << s;
        string cur;
        vector<string> temp;
        while (ss >> cur)
            temp.push_back(cur);
        if (pattern.size() != temp.size())
            return false;
        
        unordered_map<char, string> c2s;
        unordered_set<string> sUsed;
        for (int i = 0; i < pattern.size(); i++) {
            char c = pattern[i];
            cur = temp[i];
            auto it1 = c2s.find(c);
            auto it2 = sUsed.find(cur);
            if (it1 != c2s.end() && it1->second != cur || it1 == c2s.end() && it2 != sUsed.end())
                return false;
            c2s[c] = cur;
            sUsed.insert(cur);
        }
        
        return true;
    }
};