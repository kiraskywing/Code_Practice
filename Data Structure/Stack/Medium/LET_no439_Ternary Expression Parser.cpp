class Solution {
public:
    string parseTernary(string expression) {
        stack<char> s;
        int n = expression.size();
        for (int i = n - 1; i >= 0; i--) {
            if (expression[i] == '?') {
                if (expression[i - 1] == 'F')
                    s.pop();
                else {
                    char first = s.top();
                    s.pop();
                    s.pop();
                    s.push(first);
                }
                i--;
            }
            else if (expression[i] != ':') 
                s.push(expression[i]);
        }

        return string(1, s.top());
    }
};