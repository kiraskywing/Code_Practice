class Solution {
public:
    int maximumBags(vector<int>& capacity, vector<int>& rocks, int additionalRocks) {
        for (int i = 0; i < capacity.size(); i++)
            capacity[i] -= rocks[i];
        
        sort(capacity.begin(), capacity.end());
        int res = 0;
        for (int num : capacity) {
            if (num > additionalRocks)
                break;
            additionalRocks -= num;
            if (additionalRocks >= 0)
                res++;
        }

        return res;
    }
};