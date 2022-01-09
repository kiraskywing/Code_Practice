class Solution {
public:
    bool isRobotBounded(string instructions) {
        int i = 0, j = 0, d = 0;
        vector<vector<int>> moves = {{0, 1}, {1, 0}, {0, -1}, {-1, 0}};
        for (char c : instructions) {
            if (c == 'R')
                d = (d + 1) % 4;
            if (c == 'L')
                d = (d + 3) % 4;
            if (c == 'G') {
                i += moves[d][0];
                j += moves[d][1];
            }
        }
        return i == 0 && j == 0 || d != 0;
    }
};