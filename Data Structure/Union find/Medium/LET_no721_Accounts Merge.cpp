class Solution {
public:
    vector<vector<string>> accountsMerge(vector<vector<string>>& accounts) {
        vector<int> parent(accounts.size(), 0);
        map<string, int> email_id;
        for (int i = 0; i < accounts.size(); i++) {
            parent[i] = i;
            for (int j = 1; j < accounts[i].size(); j++) {
                auto it = email_id.find(accounts[i][j]);
                if (it != email_id.end()) {
                    int p1 = find(parent, i);
                    int p2 = find(parent, it->second);
                    parent[p1] = p2;
                }
                else
                    email_id[accounts[i][j]] = i;
            }
        }
        
        unordered_map<int, vector<string>> mres;
        for (auto& it : email_id) {
            int p = find(parent, it.second);
            mres[p].push_back(it.first);
        }
        
        vector<vector<string>> res;
        for (auto& it : mres) {
            vector<string> temp = {accounts[it.first][0]};
            for (auto& i : it.second)
                temp.push_back(i);
            res.push_back(temp);
        }
        return res;
    }
    
    int find(vector<int>& parent, int i) {
        if (parent[i] != i)
            parent[i] = find(parent, parent[i]);
        return parent[i];
    }
};