class SmallestInfiniteSet {
private:
    int cur;
    set<int> bucket;
public:
    SmallestInfiniteSet() { cur = 1; }
    
    int popSmallest() {
        if (bucket.empty()) {
            cur++;
            return cur - 1;
        }
        else {
            int res = *bucket.begin();
            bucket.erase(res);
            return res;
        }
    }
    
    void addBack(int num) {
        if (num < cur)
            bucket.insert(num);
    }
};

/**
 * Your SmallestInfiniteSet object will be instantiated and called as such:
 * SmallestInfiniteSet* obj = new SmallestInfiniteSet();
 * int param_1 = obj->popSmallest();
 * obj->addBack(num);
 */