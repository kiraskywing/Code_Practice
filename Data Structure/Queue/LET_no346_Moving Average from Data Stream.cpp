class MovingAverage {
public:
    queue<int> q;
    int size, count, total;
    MovingAverage(int size) {
        this->size = size;
        count = total = 0;
    }
    
    double next(int val) {
        if (count == size) {
            int evict = q.front();
            q.pop();
            total -= evict;
            count--;
        }
        
        q.push(val);
        total += val;
        count++;
        return total * 1.0 / count;
    }
};

/**
 * Your MovingAverage object will be instantiated and called as such:
 * MovingAverage* obj = new MovingAverage(size);
 * double param_1 = obj->next(val);
 */