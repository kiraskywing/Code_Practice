class Solution {
public:
    vector<int> intersection(vector<int>& nums1, vector<int>& nums2) {
        set<int> set1, set2;
        for (int num : nums1) set1.insert(num);
        for (int num : nums2) set2.insert(num);
        
        vector<int> res;
        auto iter1 = set1.begin(), iter2 = set2.begin();
        while (iter1 != set1.end() && iter2 != set2.end()) {
            if (*iter1 == *iter2) {
                res.push_back(*iter1);
                iter1++;
                iter2++;
            }
            else if (*iter1 < *iter2)
                iter1++;
            else
                iter2++;
        }

        return res;
    }
};