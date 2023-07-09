class Solution {
public:
    int lengthOfLongestSubstringKDistinct(string s, int k) {
        if (k == 0)
            return 0;

        unordered_map<int, int> memo;
        int res = 0;
        
        for (int left = 0, right = 0; right < s.size(); right++) {
            memo[s[right]]++;
            while (left < right && memo.size() > k) {
                if (--memo[s[left]] == 0)
                    memo.erase(memo.find(s[left]));
                left++;
            }

            res = max(res, right - left + 1);
        }

        return res;
    }
};