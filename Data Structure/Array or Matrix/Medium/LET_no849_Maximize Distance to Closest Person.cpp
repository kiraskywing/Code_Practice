class Solution {
public:
    int maxDistToClosest(vector<int>& seats) {
        int res = 0, pre = -1, n = seats.size();
        for (int i = 0; i < n; i++) {
            if (seats[i]) {
                res = max(res, pre < 0 ? i : (i - pre) / 2);
                pre = i;
            }
        }
        return max(res, n - 1 - pre);
    }
};