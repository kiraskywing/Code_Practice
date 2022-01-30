class Solution {
public:
    int maxNumberOfBalloons(string text) {
        unordered_map<char, int> record, letters = {{'b', 1}, {'a', 1}, {'l', 2}, {'o', 2}, {'n', 1}};
        
        for (char c : text)
            record[c] = !record.count(c) ? 1 : record[c] + 1;
        
        int res = text.size() / 7;
        for (auto& it : letters)
            res = min(res, record[it.first] / it.second);
        return res;
    }
};