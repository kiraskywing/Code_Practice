class FirstUnique {
private:
    list<int> q;
    unordered_map<int, list<int>::iterator> key2itr;
    unordered_set<int> duplicates;
public:
    FirstUnique(vector<int>& nums) {
        for (int num : nums)
            add(num);
    }
    
    int showFirstUnique() {
        return !key2itr.empty() ? q.front() : -1;
    }
    
    void add(int value) {
        if (duplicates.count(value))
            return;
        else if (key2itr.count(value)) {
            duplicates.insert(value);
            auto it = key2itr[value];
            q.erase(it);
            key2itr.erase(value);
        }
        else {
            q.push_back(value);
            key2itr[value] = --q.end();
        }
    }
};

/**
 * Your FirstUnique object will be instantiated and called as such:
 * FirstUnique* obj = new FirstUnique(nums);
 * int param_1 = obj->showFirstUnique();
 * obj->add(value);
 */