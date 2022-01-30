class RandomizedSet {
private:
    unordered_map<int, int> container;
    vector<int> list;
public:
    RandomizedSet() {}
    
    bool insert(int val) {
        if (container.count(val))
            return false;
        list.push_back(val);
        container[val] = list.size() - 1;
        return true;
    }
    
    bool remove(int val) {
        auto it = container.find(val);
        if (it == container.end())
            return false;
        int index = it->second;
        list[index] = list.back();
        list.pop_back();
        container[list[index]] = index;
        container.erase(val);
        return true;
    }
    
    int getRandom() {
        return list[rand() % list.size()];
    }
};

/**
 * Your RandomizedSet object will be instantiated and called as such:
 * RandomizedSet* obj = new RandomizedSet();
 * bool param_1 = obj->insert(val);
 * bool param_2 = obj->remove(val);
 * int param_3 = obj->getRandom();
 */