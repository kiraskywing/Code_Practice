class Solution {
public:
    int minCostToMoveChips(vector<int>& position) {
        int odd = 0, n = position.size();
        for (int i : position) 
            odd += i & 1;
        
        return min(odd, n - odd);
    }
};