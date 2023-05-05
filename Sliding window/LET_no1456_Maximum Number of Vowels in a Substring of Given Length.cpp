class Solution {
public:
    int maxVowels(string s, int k) {
        int count = 0;
        int res = 0;
        unordered_set<char> vowels = {'a', 'e', 'i', 'o', 'u'};
        for (int i = 0; i < k; i++)
            count += vowels.count(s[i]) != 0;
        res = count;

        for (int i = k; i < s.size(); i++) {
            count += vowels.count(s[i]) != 0;
            count -= vowels.count(s[i - k]) != 0;
            res = max(res, count);
        }

        return res;
    }
};