class LRUCache {
private:
    int capacity;
    list<pair<int, int>> lru_list;
    unordered_map<int, list<pair<int, int>>::iterator> memo;

public:
    LRUCache(int capacity) : capacity{capacity} {}
    
    int get(int key) {
        if (memo.count(key) == 0)
            return -1;

        auto it_list = memo[key];
        lru_list.splice(lru_list.end(), lru_list, it_list);
        return it_list->second;
    }
    
    void put(int key, int value) {
        if (get(key) != -1) {
            memo[key]->second = value;
            return;
        }

        if (memo.size() == capacity) {
            int key_to_evict = lru_list.front().first;
            lru_list.pop_front();
            memo.erase(key_to_evict);
        }

        lru_list.push_back({key, value});
        auto it = lru_list.end();
        it--;
        memo[key] = it;
    }
};

/**
 * Your LRUCache object will be instantiated and called as such:
 * LRUCache* obj = new LRUCache(capacity);
 * int param_1 = obj->get(key);
 * obj->put(key,value);
 */