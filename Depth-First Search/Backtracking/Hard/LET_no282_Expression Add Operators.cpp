class Solution {
public:
    vector<string> addOperators(string num, int target) {
        vector<string> res;
        dfs(num, res, "", 0, 0, false, target);
        return res;
    }
    
    void dfs(string num, vector<string>& res, string path, long value, long prev, bool has_prev, int target) {
        if (num.size() == 0) {
            if (value == target)
                res.push_back(path);
            return;
        }
        
        for (int i = 1; i <= num.size(); i++) {
            if (i == 1 || i > 1 && num[0] != '0') {
                long temp = stol(num.substr(0,i));
                if (!has_prev)
                    dfs(num.substr(i), res, num.substr(0, i), temp, temp, true, target);
                else {
                    dfs(num.substr(i), res, path + "+" + num.substr(0, i), value + temp, temp, has_prev, target);
                    dfs(num.substr(i), res, path + "-" + num.substr(0, i), value - temp, -temp, has_prev, target);
                    dfs(num.substr(i), res, path + "*" + num.substr(0, i), value - prev + prev * temp, prev * temp, has_prev, target);
                }
            }
        }
    }
};