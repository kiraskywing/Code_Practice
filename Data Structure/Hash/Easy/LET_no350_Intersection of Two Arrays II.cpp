class Solution {
public:
    vector<int> intersect(vector<int>& nums1, vector<int>& nums2) {
        unordered_map<int, int> record;
        for (int i : nums1)
            record[i]++;
        
        vector<int> res;
        for (int i : nums2) {
            if (record[i]-- > 0)
                res.push_back(i);
        }
        return res;
    }
};