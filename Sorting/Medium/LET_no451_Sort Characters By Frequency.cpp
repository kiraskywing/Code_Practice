class Solution {
public:
    string frequencySort(string s) {
        unordered_map<char, int> table;
        for (char c : s)
            table[c] += 1;
        
        map<int, string> substring;
        for (auto p : table) {
            char c = p.first;
            int n = p.second;
            substring[n] += string(n, c);
        }
        
        string res;
        for (auto rit = substring.rbegin(); rit != substring.rend(); rit++)
            res += rit->second;
        return res;
    }
};