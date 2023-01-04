class Solution {
public:
    int minimumRounds(vector<int>& tasks) {
        unordered_map<int, int> memo;
        for (int num : tasks) {
            auto it = memo.find(num);
            if (it == memo.end()) 
                memo[num] = 1;
            else
                it->second++;
        }

        int res = 0;
        for (auto it = memo.begin(); it != memo.end(); it++) {
            int count = it->second;
            if (count < 2)
                return -1;
            res += (count + 2) / 3;
        }

        return res;
    }
};