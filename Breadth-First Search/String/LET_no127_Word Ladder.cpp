class Solution {
public:
    int ladderLength(string beginWord, string endWord, vector<string>& wordList) {
        unordered_set<string> memo(wordList.begin(), wordList.end());
        if (!memo.count(endWord))
            return 0;

        unordered_set<string> visited({beginWord});
        queue<string> q;
        q.push(beginWord);
        int times = 1;

        while (!q.empty()) {
            int n = q.size();
            while (n-- > 0) {
                string cur = q.front();
                q.pop();

                if (cur == endWord)
                    return times;
                
                for (int i = 0; i < cur.size(); i++) {
                    char c = cur[i];
                    
                    for (int d = 0; d < 26; d++) {
                        char c2 = 'a' + d;
                        if (c2 == cur[i])
                            continue;
                        
                        cur[i] = c2;
                        if (memo.count(cur) && !visited.count(cur)) {
                            visited.insert(cur);
                            q.push(cur);
                        }
                    }

                    cur[i] = c;
                }
            }

            times++;
        }

        return 0;
    }
};