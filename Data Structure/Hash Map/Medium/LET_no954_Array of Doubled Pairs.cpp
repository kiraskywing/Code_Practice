class Solution {
public:
    bool canReorderDoubled(vector<int>& arr) {
        unordered_map<int, int> record;
        for (int num : arr)
            record[num]++;
        
        vector<int> keys;
        for (auto it : record)
            keys.push_back(it.first);
        
        sort(keys.begin(), keys.end(), [](int i, int j) {return abs(i) < abs(j);});
        for (int key : keys) {
            if (record[key] > record[key * 2])
                return false;
            record[key * 2] -= record[key];
        }
        
        return true;
    }
};