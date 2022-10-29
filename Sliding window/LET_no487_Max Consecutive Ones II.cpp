class Solution {
public:
    int findMaxConsecutiveOnes(vector<int>& nums) {
        int prev = -1;
        int cur = 0;
        int res = 0;
        
        for (int &num : nums) {
            if (num == 0) {
                prev = cur;
                cur = 0;
            }
            else 
                cur++;
            
            res = max(res, prev + cur + 1);
        }
        
        return res;
    }
};