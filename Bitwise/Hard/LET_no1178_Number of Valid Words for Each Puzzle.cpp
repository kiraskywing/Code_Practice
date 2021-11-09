class Solution {
public:
    vector<int> findNumOfValidWords(vector<string>& words, vector<string>& puzzles) {
        unordered_map<int, int> table;
        for (string& w : words) {
            int mask = getMask(w);
            table[mask]++;
        }
        
        int n = words.size();
        vector<int> res;
        for (string& w : puzzles) {
            int mask = getMask(w);
            int firstChar = 1 << (w[0] - 'a');
            int cur = 0;
            
            for (int sub = mask; sub > 0; sub = ((sub - 1) & mask)) {
                if ((sub & firstChar) && table.count(sub)) {
                    auto it = table.find(sub);
                    if (it != table.end())
                        cur += it->second;
                }
            }
            res.push_back(cur);
        }
        
        return res;
    }
    
    int getMask(string& w) {
        int res = 0;
        for (char c : w)
            res |= (1 << (c - 'a'));
        return res;
    }
};