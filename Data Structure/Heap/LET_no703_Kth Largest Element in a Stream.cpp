class KthLargest {
private:
    priority_queue<int> pq;
    int size;
public:
    KthLargest(int k, vector<int>& nums) {
        size = k;
        for (int num : nums)
            pq.push(-num);
    }
    
    int add(int val) {
        pq.push(-val);
        while (pq.size() > size)
            pq.pop();
        return -pq.top();
    }
};

/**
 * Your KthLargest object will be instantiated and called as such:
 * KthLargest* obj = new KthLargest(k, nums);
 * int param_1 = obj->add(val);
 */