class Solution {
public:
    vector<vector<string>> findLadders(string beginWord, string endWord, vector<string>& wordList) {
        unordered_set<string> wordset(wordList.begin(), wordList.end());
        if (!wordset.count(endWord))
            return {};
        
        wordset.insert(beginWord);
        unordered_map<string, int> distance = buildGraph(endWord, beginWord, wordset);
        if (!distance.count(beginWord))
            return {};

        vector<vector<string>> res;
        vector<string> temp = {beginWord};
        helper(distance, wordset, temp, res);
        return res;
    }

    unordered_map<string, int> buildGraph(string& start, string& end, unordered_set<string>& wordset) {
        unordered_map<string, int> distance;
        distance[start] = 0;
        queue<string> q;
        q.push(start);

        while (!q.empty()) {
            string cur = q.front();
            q.pop();
            if (distance.count(end) && distance[cur] > distance[end])
                continue;
            vector<string> next_words = getNextWords(cur, wordset);
            for (string& s : next_words) {
                if (!distance.count(s)) {
                    distance[s] = distance[cur] + 1;
                    q.push(s);
                }
            }
        }

        return distance;
    }

    vector<string> getNextWords(string& cur, unordered_set<string>& wordset) {
        vector<string> res;
        for (int i = 0; i < cur.size(); i++) {
            for (int d = 0; d < 26; d++) {
                char c = 'a' + d;
                if (c == cur[i])
                    continue;
                char temp = cur[i];
                cur[i] = c;
                if (wordset.count(cur))
                    res.push_back(cur);
                cur[i] = temp;
            }
        }
        return res;
    }

    void helper(unordered_map<string, int>& distance, unordered_set<string>& wordset, vector<string>& temp, vector<vector<string>>& res) {
        string cur = temp.back();
        if (distance[cur] == 0) {
            res.push_back(temp);
            return;
        }

        vector<string> next_words = getNextWords(cur, wordset);
        for (string& s : next_words) {
            if (distance.count(s) && distance[s] == distance[cur] - 1) {
                temp.push_back(s);
                helper(distance, wordset, temp, res);
                temp.pop_back();
            }
        }
    }
};