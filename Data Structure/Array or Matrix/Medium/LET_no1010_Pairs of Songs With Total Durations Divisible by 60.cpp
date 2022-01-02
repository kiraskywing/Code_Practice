class Solution {
public:
    int numPairsDivisibleBy60(vector<int>& time) {
        int res = 0;
        vector<int> modTable(60, 0);
        for (int t : time) {
            res += modTable[(60 - t % 60) % 60];
            modTable[t % 60]++;
        }
        return res;
    }
};