class Solution {
public:
    string decodeString(string s) {
        stack<int> stack_nums;
        stack<string> stack_strs;
        int num = 0;
        string cur_str = "";
        
        for (char c : s) {
            if (c == '[') {
                stack_nums.push(num);
                stack_strs.push(cur_str);
                num = 0;
                cur_str = "";
            }
            else if (c == ']') {
                int pre_num = stack_nums.top();
                stack_nums.pop();
                string pre_str = stack_strs.top();
                stack_strs.pop();
                for (int i = 0; i < pre_num; i++)
                    pre_str.append(cur_str);
                cur_str = pre_str;
            }
            else if (isdigit(c))
                num = num * 10 + c - '0';
            else
                cur_str += c;
        }
        
        return cur_str;
    }
};