class Trie {
private:
    unordered_map<char, Trie*> children;
    bool is_word;
public:
    Trie() { is_word = false; }
    
    void insert(string word) {
        Trie* cur = this;
        for (char c : word) {
            if (!cur->children.count(c))
                cur->children[c] = new Trie();
            cur = cur->children[c];
        }
        cur->is_word = true;
    }
    
    bool search(string word) {
        Trie* cur = this;
        for (char c : word) {
            if (!cur->children.count(c))
                return false;
            cur = cur->children[c];
        }
        return cur->is_word;
    }
    
    bool startsWith(string prefix) {
        Trie* cur = this;
        for (char c : prefix) {
            if (!cur->children.count(c))
                return false;
            cur = cur->children[c];
        }
        return true;
    }
};

/**
 * Your Trie object will be instantiated and called as such:
 * Trie* obj = new Trie();
 * obj->insert(word);
 * bool param_2 = obj->search(word);
 * bool param_3 = obj->startsWith(prefix);
 */