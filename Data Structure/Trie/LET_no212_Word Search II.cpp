class Trie {
public:
    bool is_word;
    unordered_map<char, Trie*> children;
    
    Trie() { is_word = false; }
    void insert(string& word) {
        Trie* cur = this;
        for (char c : word) {
            if (!cur->children.count(c))
                cur->children[c] = new Trie();
            cur = cur->children[c];
        }
        cur->is_word = true;
    }
    bool search(string& word) {
        Trie* cur = this;
        for (char c : word) {
            if (!cur->children.count(c))
                return false;
            cur = cur->children[c];
        }
        return cur->is_word;
    }
};

class Solution {
public:
    vector<string> findWords(vector<vector<char>>& board, vector<string>& words) {
        vector<string> res;
        Trie trie;
        for (string& w : words)
            trie.insert(w);
        Trie* root = &trie;
        for (int i = 0; i < board.size(); i++) {
            for (int j = 0; j < board[0].size(); j++)
                dfs(board, i, j, root, "", res);
        }
        return res;
    }
    
    void dfs(vector<vector<char>>& board, int i, int j, Trie* cur, string s, vector<string>& res) {
        if (cur->is_word) {
            res.push_back(s);
            cur->is_word = false;
        }
        if (!(0 <= i && i < board.size() && 0 <= j && j < board[0].size()))
            return;
        
        char temp = board[i][j];
        if (!(cur->children.count(temp)))
            return;
        cur = cur->children[temp];
        board[i][j] = '*';
        dfs(board, i + 1, j, cur, s + temp, res);
        dfs(board, i - 1, j, cur, s + temp, res);
        dfs(board, i, j + 1, cur, s + temp, res);
        dfs(board, i, j - 1, cur, s + temp, res);
        board[i][j] = temp;
    }
};