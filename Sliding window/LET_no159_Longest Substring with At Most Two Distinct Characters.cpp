class Solution {
public:
    int lengthOfLongestSubstringTwoDistinct(string s) {
        unordered_map<char, int> memo;
        int i = 0, j = 0, left = 0;
        for (int right = 0; right < s.size(); right++) {
            memo[s[right]]++;
            while (memo.size() > 2 && left + 1 < right) {
                memo[s[left]]--;
                if (memo[s[left]] == 0)
                    memo.erase(s[left]);
                left++;
            }

            if (right - left > j - i) {
                i = left;
                j = right;
            }
        }

        return j - i + 1;
    }
};