class Solution {
public:
    bool detectCapitalUse(string word) {
        int caps = 0;
        for (char c : word)
            caps += 'A' <= c && c <= 'Z';
        
        return caps == word.size() || caps == 0 || caps == 1 && 'A' <= word[0] && word[0] <= 'Z';
    }
};