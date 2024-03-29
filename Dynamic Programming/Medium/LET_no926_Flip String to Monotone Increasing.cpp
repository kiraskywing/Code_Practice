class Solution {
public:
    int minFlipsMonoIncr(string s) {
        int ones = 0, flips = 0;
        for (char c : s) {
            if (c == '1')
                ones++;
            else
                flips++;
            flips = min(ones, flips);
        }
        return flips;
    }
};