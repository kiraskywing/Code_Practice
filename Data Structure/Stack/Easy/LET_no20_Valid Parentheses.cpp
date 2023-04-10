class Solution {
public:
    bool isValid(string s) {
        vector<char> stk;
        for (char c : s) {
            if (!stk.empty()) {
                char c2 = stk.back();
                if (c2 == '(' && c == ')' ||
                    c2 == '{' && c == '}' ||
                    c2 == '[' && c == ']') 
                        stk.pop_back();
                else
                    stk.push_back(c);
            }
            else
                stk.push_back(c);
        }

        return stk.empty();
    }
};