class Solution {
public:
    int canCompleteCircuit(vector<int>& gas, vector<int>& cost) {
        int n = gas.size();
        for (int i = 0; i < n; i++)
            gas[i] -= cost[i];

        if (accumulate(gas.begin(), gas.end(), 0) < 0)
            return -1;

        int start = 0, cur = 0;
        for (int i = 0; i < n; i++) {
            cur += gas[i];
            if (cur < 0) {
                cur = 0;
                start = i + 1;
            }
        }

        return start;
    }
};