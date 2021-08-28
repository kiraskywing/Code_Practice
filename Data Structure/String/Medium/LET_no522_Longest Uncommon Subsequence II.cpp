class Solution {
public:
    int findLUSlength(vector<string>& strs) {
        sort(strs.begin(), strs.end(), [](string& a, string& b) { return a.size() > b.size(); });
        for (string& sub : strs) {
            int count = 0;
            for (string& target : strs)
                count += issubsequence(sub, target);
            if (count == 1)
                return sub.size();
        }
        return -1;
    }
    
    int issubsequence(string& sub, string& target) {
        int i = 0;
        for (char c : target) {
            if (c == sub[i])
                i++;
        }
        return i == sub.size();
    }
};