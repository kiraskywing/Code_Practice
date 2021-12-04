class Trie {
public:
    unordered_map<char, Trie*> children;
    bool isEnd;
    
    Trie() { isEnd = false; }
    
    void insert(string& word) {
        Trie* cur = this;
        for (int i = word.size() - 1; i >= 0; i--) {
            char c = word[i];
            if (!cur->children.count(c))
                cur->children[c] = new Trie();
            cur = cur->children[c];
        }
        cur->isEnd = true;
    }
};

class StreamChecker {
private:
    vector<char> letters;
    Trie* trie;
public:
    StreamChecker(vector<string>& words) {
        trie = new Trie();
        for (string& w : words)
            trie->insert(w);
    }
    
    bool query(char letter) {
        letters.push_back(letter);
        Trie* cur = trie;
        for (int i = letters.size() - 1; i >= 0; i--) {
            char c = letters[i];
            if (cur->isEnd)
                return true;
            if (!cur->children.count(c))
                return false;
            cur = cur->children[c];
        }
        return cur->isEnd;
    }
};

/**
 * Your StreamChecker object will be instantiated and called as such:
 * StreamChecker* obj = new StreamChecker(words);
 * bool param_1 = obj->query(letter);
 */