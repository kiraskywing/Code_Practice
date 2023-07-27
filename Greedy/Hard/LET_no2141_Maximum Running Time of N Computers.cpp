class Solution {
public:
    long long maxRunTime(int n, vector<int>& batteries) {
        sort(batteries.begin(), batteries.end());
        long long total = accumulate(batteries.begin(), batteries.end(), 0L);
        int size = batteries.size(), k = 0;
        while (batteries[size - 1 - k] > total / (n - k))
            total -= batteries[size - 1 - k++];

        return total / (n - k);
    }
};  