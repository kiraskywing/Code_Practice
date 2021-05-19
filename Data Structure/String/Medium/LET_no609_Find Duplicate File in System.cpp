class Solution {
public:
    vector<vector<string>> findDuplicate(vector<string>& paths) {
        unordered_map<string, vector<string>> records;
        vector<vector<string>> res;
        
        for (auto path : paths) {
            stringstream ss(path);
            string root;
            string s;
            getline(ss, root, ' ');
            while (getline(ss, s, ' ')) {
                string fileName = s.substr(0, s.find('('));
                string content = s.substr(s.find('(') + 1, s.find(')') - s.find('(') - 1);
                records[content].push_back(root + "/" + fileName);
            }
        }
        
        for (auto path : records) {
            if (path.second.size() >= 2)
                res.push_back(path.second);
        }
        
        return res;
    }
};