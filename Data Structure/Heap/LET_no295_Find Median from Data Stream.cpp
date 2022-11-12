class MedianFinder {
private: 
    priority_queue<int> first, second;
public:
    MedianFinder() {}
    
    void addNum(int num) {
        first.push(num);
        second.push(-first.top());
        first.pop();
        
        if (second.size() > first.size()) {
            first.push(-second.top());
            second.pop();
        }
    }
    
    double findMedian() {
        return first.size() > second.size() ? first.top() : (first.top() + (-second.top())) / 2.0;
    }
};

/**
 * Your MedianFinder object will be instantiated and called as such:
 * MedianFinder* obj = new MedianFinder();
 * obj->addNum(num);
 * double param_2 = obj->findMedian();
 */