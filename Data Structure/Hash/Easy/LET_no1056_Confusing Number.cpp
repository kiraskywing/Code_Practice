class Solution {
public:
    bool confusingNumber(int n) {
        unordered_map<int, int> memo = {{0, 0}, {1, 1}, {6, 9}, {8, 8}, {9, 6}};
        int new_num = 0, prev = n;
        while (n > 0) {
            int cur = n % 10;
            auto it = memo.find(cur);
            if (it == memo.end())
                return false;
            new_num = new_num * 10 + it->second;
            n /= 10;
        }
        
        return prev != new_num;
    }
};