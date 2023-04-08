class Solution {
public:
    vector<int> anagramMappings(vector<int>& nums1, vector<int>& nums2) {
        unordered_map<int, vector<int>> memo;
        for (int i = 0; i < nums1.size(); i++)
            memo[nums1[i]].push_back(i);

        vector<int> res(nums1.size());
        
        for (int j = 0; j < nums2.size(); j++) {
            int num = nums2[j];
            res[memo[num].back()] = j;
            memo[num].pop_back();
        }

        return res;
    }
};