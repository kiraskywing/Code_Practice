class Solution {
public:
    vector<vector<int>> findDifference(vector<int>& nums1, vector<int>& nums2) {
        unordered_set<int> memo1(nums1.begin(), nums1.end()), memo2(nums2.begin(), nums2.end());
        vector<vector<int>> res(2, vector<int>());

        for (int num : memo1) {
            if (memo2.count(num) == 0)
                res[0].push_back(num);
        }

        for (int num : memo2) {
            if (memo1.count(num) == 0)
                res[1].push_back(num);
        }

        return res;
    }
};