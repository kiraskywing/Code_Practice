class Solution {
public:
    bool judgeSquareSum(int c) {
        unordered_set<int> record;
        for (int i = 0; i <= sqrt(c); i++) {
            record.insert(i * i);
            if (record.find(c - i * i) != record.end())
                return true;
        }
        return false;
    }
};