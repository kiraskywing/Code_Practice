class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        unordered_map<string, vector<string>> mp;
        for (string s : strs)
            mp[bucketSort(s)].push_back(s);
        
        vector<vector<string>> res;
        for (auto p : mp)
            res.push_back(p.second);
        
        return res;
    }
    
    string bucketSort(string& s) {
        vector<int> counts(26, 0);
        for (char c : s)
            counts[c - 'a']++;
        
        string res;
        for (int i = 0; i < 26; i++)
            res += string(counts[i], 'a' + i);
        
        return res;
    }
};