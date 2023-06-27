class TwoSum {
private:
    unordered_map<long, int> memo;
public:
    TwoSum() { }
    
    void add(int number) {
        memo[long(number)]++;
    }
    
    bool find(int value) {
        for (auto it : memo) {
            long cur = it.first;
            int count = it.second;
            long target = long(value) - cur;
            if (memo.count(target) && (target != cur || count > 1))
                return true;
        }

        return false;
    }
};

/**
 * Your TwoSum object will be instantiated and called as such:
 * TwoSum* obj = new TwoSum();
 * obj->add(number);
 * bool param_2 = obj->find(value);
 */