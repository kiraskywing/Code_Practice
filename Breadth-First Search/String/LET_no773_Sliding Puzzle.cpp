class Solution {
public:
    int slidingPuzzle(vector<vector<int>>& board) {
        int steps = 0;
        string dest = "123450";
        vector<vector<int>> next_move = {{1,3}, {0,2,4}, {1,5}, {0,4}, {1,3,5}, {2,4}};
        /*
        0 | 1 | 2
        ---------
        3 | 4 | 5
        */

        string start = "";
        for (auto& row : board) {
            for (int num : row)
                start += to_string(num);
        }

        unordered_set<string> visited({start});
        queue<string> q;
        q.push(start);

        while (!q.empty()) {
            int n = q.size();
            while (n-- > 0) {
                string cur = q.front();
                q.pop();

                if (cur == dest)
                    return steps;

                int idx = cur.find("0");
                for (int idx2 : next_move[idx]) {
                    swap(cur[idx], cur[idx2]);
                    if (!visited.count(cur)) {
                        visited.insert(cur);
                        q.push(cur);
                    }
                    swap(cur[idx], cur[idx2]);
                }
            }
            
            steps++;
        }

        return -1;
    }
};