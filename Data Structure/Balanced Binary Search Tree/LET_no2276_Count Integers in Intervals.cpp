class CountIntervals {
public:
    map<int, int> m;
    int total = 0;
    
    void add(int left, int right) {
        auto it = m.upper_bound(left);
        if (it != m.begin()) {
            auto p = prev(it);
            if (p->second >= left) {
                left = p->first;
                right = max(right, p->second);
                total -= p->second - p->first + 1;
                m.erase(p);
            }
        }
        
        for (; it != m.end() && it->first <= right; m.erase(it++)) {
            right = max(right, it->second);
            total -= it->second - it->first + 1;
        }
        
        total += right - left + 1;
        m[left] = right;
    }
    
    int count() {
        return total;
    }
};

/**
 * Your CountIntervals object will be instantiated and called as such:
 * CountIntervals* obj = new CountIntervals();
 * obj->add(left,right);
 * int param_2 = obj->count();
 */