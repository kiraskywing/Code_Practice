class Solution {
public:
    int calculate(string s) {
        vector<pair<int, int>> stack;
        int res = 0, sign = 1, num = 0;
        for (char c : s) {
            if (c >= '0')
                num = num * 10 + (c - '0');
            else if (c == '+' or c == '-') {
                res += sign * num;
                sign = c == '+' ? 1 : -1;
                num = 0;
            }
            else if (c == '(') {
                stack.push_back({res, sign});
                res = 0;
                sign = 1;
            }
            else if (c == ')') {
                res += sign * num;
                num = 0;
                pair<int, int> prev = stack.back();
                res *= prev.second;
                res += prev.first;
                stack.pop_back();
            }
        }
        
        if (num > 0)
            res += sign * num;
        
        return res;
    }
};