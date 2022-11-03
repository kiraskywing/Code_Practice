class Solution {
public:
    int smallestCommonElement(vector<vector<int>>& mat) {
        vector<int> memo(10001, 0);
        int m = mat.size();
        for (auto row : mat) {
            for (int num : row) {
                memo[num]++;
                if (memo[num] == m)
                    return num;
            }
        }
        
        return -1;
    }
};