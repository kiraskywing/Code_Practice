class Solution {
public:
    int trap(vector<int>& height) {
        int left = 0, right = height.size() - 1;
        int leftMax = 0, rightMax = 0, res = 0;

        while (left < right) {
            if (height[left] < height[right]) {
                leftMax = max(leftMax, height[left]);
                res += leftMax - height[left];
                left++;
            }
            else {
                rightMax = max(rightMax, height[right]);
                res += rightMax - height[right];
                right--;
            }
        }

        return res;
    }
};