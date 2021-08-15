class Solution {
public:
    int memo[200][200][200] = {};
    
    int removeBoxes(vector<int>& boxes) {
        return dp(boxes, 0, boxes.size() - 1, 0);
    }
    
    int dp(vector<int>& boxes, int left, int right, int k) {
        if (left > right)
            return 0;
        if (memo[left][right][k] > 0)
            return memo[left][right][k];
        
        int i = left, d = k;
        while (i + 1 <= right && boxes[i] == boxes[i + 1]) {
            i++;
            d++;
        }
        
        int res = (d + 1) * (d + 1) + dp(boxes, i + 1, right, 0);
        for (int m = i + 1; m <= right; m++) {
            if (boxes[m] == boxes[i])
                res = max(res, dp(boxes, m, right, d + 1) + dp(boxes, i + 1, m - 1, 0));
        }
        
        return memo[left][right][k] = res;
    }
};