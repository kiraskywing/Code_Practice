class Solution {
public:
    int leastInterval(vector<char>& tasks, int n) {
        unordered_map<char, int> memo;
        int maxFreq = 0;
        for (char c : tasks) {
            memo[c]++;
            maxFreq = max(maxFreq, memo[c]);
        }

        int res = (maxFreq - 1) * (n + 1);
        for (auto it = memo.begin(); it != memo.end(); it++)
            res += it->second == maxFreq;

        return max(int(tasks.size()), res);
    }
};