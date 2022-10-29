class Solution {
public:
    int earliestFullBloom(vector<int>& plantTime, vector<int>& growTime) {
        vector<pair<int, int>> items;
        for (int i = 0; i < plantTime.size(); i++)
            items.push_back({growTime[i], plantTime[i]});
        
        sort(items.begin(), items.end());
        int res = 0;
        for (auto [grow, plant]: items)
            res = max(res, grow) + plant;
        
        return res;
    }
};