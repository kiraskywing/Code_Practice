class Solution {
public:
    string destCity(vector<vector<string>>& paths) {
        unordered_set<string> memo;
        for (vector<string>& path : paths)
            memo.insert(path[0]);
        for (vector<string>& path : paths) {
            if (!memo.count(path[1]))
                return path[1];
        }
            
        return "";
    }
};