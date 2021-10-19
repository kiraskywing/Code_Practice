class Solution {
public:
    vector<int> nextGreaterElement(vector<int>& nums1, vector<int>& nums2) {
        stack<int> s;
        unordered_map<int, int> table;
        for (int n : nums2) {
            while (s.size() && s.top() < n) {
                table[s.top()] = n;
                s.pop();
            }
            s.push(n);
        }
        
        int n = nums1.size();
        vector<int> res(n, -1);
        for (int i = 0; i < n; i++) {
            auto it = table.find(nums1[i]);
            if (it != table.end())
                res[i] = it->second;
        }
        return res;
    }
};