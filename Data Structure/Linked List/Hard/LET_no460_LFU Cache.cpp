class LFUCache {
private:
    int capacity, size, minFreq;
    unordered_map<int, list<int>> freq2keys;
    unordered_map<int, pair<int, int>> key2value;  // (value, freq)
    unordered_map<int, list<int>::iterator> key2pos;

public:
    LFUCache(int capacity) {
        this->capacity = capacity;
        size = minFreq = 0;
    }
    
    int get(int key) {
        if (!key2value.count(key))
            return -1;
        
        updateFreq(key);
        return key2value[key].first;
    }
    
    void put(int key, int value) {
        if (!capacity)
            return;
        
        if (key2value.count(key)) {
            key2value[key].first = value;
            updateFreq(key);
        }
        else {
            if (size == capacity) {
                int victimKey = freq2keys[minFreq].front();
                freq2keys[minFreq].pop_front();
                key2value.erase(victimKey);
                key2pos.erase(victimKey);
            }
            else
                size++;
            
            key2value[key] = {value, 1};
            freq2keys[1].push_back(key);
            key2pos[key] = --freq2keys[1].end();
            minFreq = 1;
        }
    }

    void updateFreq(int key) {
        int freq = key2value[key].second;
        auto iter = key2pos[key];
        key2value[key].second++;
        freq2keys[freq].erase(iter);
        freq2keys[freq + 1].push_back(key);
        key2pos[key] = --freq2keys[freq + 1].end();
        
        if (freq2keys[minFreq].empty())
            minFreq++;
    }
};

/**
 * Your LFUCache object will be instantiated and called as such:
 * LFUCache* obj = new LFUCache(capacity);
 * int param_1 = obj->get(key);
 * obj->put(key,value);
 */