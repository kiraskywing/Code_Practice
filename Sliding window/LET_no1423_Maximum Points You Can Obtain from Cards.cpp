class Solution {
public:
    int maxScore(vector<int>& cardPoints, int k) {
        int size = cardPoints.size() - k;
        int minSubarraySum = 0, cur = 0;
        minSubarraySum = cur = accumulate(cardPoints.begin(), cardPoints.begin() + size, 0);
        
        for (int i = 0; i < cardPoints.size() - size; i++) {
            cur += (cardPoints[i + size] - cardPoints[i]);
            minSubarraySum = min(minSubarraySum, cur);
        }
        
        return accumulate(cardPoints.begin(), cardPoints.end(), 0) - minSubarraySum;
    }
};