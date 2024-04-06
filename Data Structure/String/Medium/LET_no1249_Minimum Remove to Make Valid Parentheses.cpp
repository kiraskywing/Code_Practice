class Solution {
public:
    string minRemoveToMakeValid(string s) {
        vector<int> memo;
        unordered_set<int> removes;
        for (int i = 0; i < s.size(); i++) {
            if (s[i] == '(')
                memo.push_back(i);
            else if (s[i] == ')') {
                if (!memo.empty())
                    memo.pop_back();
                else
                    removes.insert(i);
            }
        }

        for (int i : memo)
            removes.insert(i);

        string res;
        for (int i = 0; i < s.size(); i++) {
            if (!removes.count(i))
                res.push_back(s[i]);
        }

        return res;
    }
};