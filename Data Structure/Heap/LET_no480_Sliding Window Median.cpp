class Solution {
private:
    multiset<int> left_bst, right_bst;
public:
    vector<double> medianSlidingWindow(vector<int>& nums, int k) {
        int n = nums.size();
        if (n == 0)
            return {};
        
        vector<double> res;
        for (int i = 0; i < n; i++) {
            if (left_bst.size() == 0 || nums[i] <= *left_bst.rbegin())
                left_bst.insert(nums[i]);
            else
                right_bst.insert(nums[i]);
            balance();
            
            if (i < k - 1)
                continue;
            
            res.push_back(getMedian());
            auto it = left_bst.find(nums[i - k + 1]);
            if (it != left_bst.end())
                left_bst.erase(it);
            else
                right_bst.erase(right_bst.find(nums[i - k + 1]));
        }
        
        return res;
    }
    
    void balance(void) {
        if (left_bst.size() > right_bst.size() + 1) {
            right_bst.insert(*left_bst.rbegin());
            left_bst.erase(left_bst.find(*left_bst.rbegin()));
        }
        else if (left_bst.size() < right_bst.size()) {
            left_bst.insert(*right_bst.begin());
            right_bst.erase(right_bst.find(*right_bst.begin()));
        }
    }
    
    double getMedian(void) {
        if (left_bst.size() == right_bst.size())
            return (*left_bst.rbegin() * 1.0 + *right_bst.begin() * 1.0) / 2;
        return *left_bst.rbegin() * 1.0;
    }
};