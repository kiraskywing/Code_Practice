class Node {
public:
    unordered_map<char, Node*> children;
    vector<string> word_list;
};

class Trie {
public:
    Node* root;
    
    void insert(string& word) {
        Node* cur = this->root;
        for (char c : word) {
            if (!cur->children.count(c))
                cur->children[c] = new Node();
            cur = cur->children[c];
            cur->word_list.push_back(word);
        }
    }

    Node* find(string& word) {
        Node* cur = this->root;
        for (char c : word) {
            if (!cur->children.count(c))
                return nullptr;
            cur = cur->children[c];
        }
        return cur;
    }

    vector<string> prefix2wordlist(string& prefix) {
        Node* cur = find(prefix);
        return !cur ? vector<string>() : cur->word_list;
    }

    Trie(vector<string>& words) {
        this->root = new Node();
        for (string& word : words)
            insert(word);
    }
};

class Solution {
public:
    vector<vector<string>> wordSquares(vector<string>& words) {
        Trie trie(words);
        vector<vector<string>> res;
        vector<string> square;
        for (string& word : words) {
            square.push_back(word);
            dfs(trie, square, res);
            square.pop_back();
        }

        return res;
    }

    void dfs(Trie& trie, vector<string>& square, vector<vector<string>>& res) {
        int m = square.size(), n = square[0].size();
        if (m == n) {
            res.push_back(square);
            return;
        }

        string prefix;
        for (int i = 0; i < m; i++)
            prefix.push_back(square[i][m]);
        vector<string> candidates = trie.prefix2wordlist(prefix);
        
        for (string& word : candidates) {
            if (!checkPrefix(word, trie, square))
                continue;
            square.push_back(word);
            dfs(trie, square, res);
            square.pop_back();
        }
    }

    bool checkPrefix(string& word, Trie& trie, vector<string>& square) {
        int m = square.size(), n = square[0].size();
        for (int j = m + 1; j < n; j++) {
            string prefix;
            for (int i = 0; i < m; i++)
                prefix.push_back(square[i][j]);
            prefix.push_back(word[j]);
            if (!trie.find(prefix))
                return false;            
        }
        return true;
    }
};