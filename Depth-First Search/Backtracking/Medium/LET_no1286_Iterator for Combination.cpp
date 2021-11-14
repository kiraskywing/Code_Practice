class CombinationIterator {
private:
    vector<int> idx;
    string s;
public:
    CombinationIterator(string characters, int combinationLength) {
        s = characters;
        for (int i = 0; i < combinationLength; i++)
            idx.push_back(i);
    }
    
    string next() {
        string res;
        for (int i = 0; i < idx.size(); i++)
            res += s[idx[i]];
        
        idx.back()++;
        if (idx.back() < s.size())
            return res;
        
        for (int i = idx.size() - 2, remain = 2; i >= 0; i--, remain++) {
            if (idx[i] + remain < s.size()) {
                idx[i]++;
                for (int j = i + 1; j < idx.size(); j++)
                    idx[j] = idx[j - 1] + 1;
                return res;
            }
        }
        
        idx[0] = -1;
        return res;
    }
    
    bool hasNext() {
        return idx[0] != -1;
    }
};

/**
 * Your CombinationIterator object will be instantiated and called as such:
 * CombinationIterator* obj = new CombinationIterator(characters, combinationLength);
 * string param_1 = obj->next();
 * bool param_2 = obj->hasNext();
 */