class Solution {
public:
    bool isPathCrossing(string path) {
        int x = 0, y = 0;
        set<pair<int, int>> memo;
        memo.insert({0, 0});
        for (char c : path) {
            switch (c) {
                case 'N': 
                    y++;
                    break;
                case 'S': 
                    y--;
                    break;
                case 'E': 
                    x++;
                    break;
                case 'W': 
                    x--;
                    break;
                default:
                    break;
            }

            if (memo.count({x, y}))
                return true;
            memo.insert({x, y});
        }

        return false;
    }
};