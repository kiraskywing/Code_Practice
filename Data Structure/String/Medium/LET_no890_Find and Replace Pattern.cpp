class Solution {
public:
    vector<string> findAndReplacePattern(vector<string>& words, string pattern) {
        vector<string> res;
        for (string& w : words) {
            if (w.size() != pattern.size()) continue;
            unordered_map<char, char> w2p, p2w;
            bool valid = true;
            for (int i = 0; i < w.size(); i++) {
                if (!w2p.count(w[i]) and !p2w.count(pattern[i])) {
                    w2p[w[i]] = pattern[i];
                    p2w[pattern[i]] = w[i];
                }
                else {
                    if (w2p.count(w[i]) && w2p[w[i]] != pattern[i] 
                        || p2w.count(pattern[i]) && p2w[pattern[i]] != w[i]) {
                        valid = false;
                        break;
                    }
                }
            }
            if (valid) res.push_back(w);
        }
        
        return res;
    }
};