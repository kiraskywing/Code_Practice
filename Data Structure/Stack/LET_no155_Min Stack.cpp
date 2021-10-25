class MinStack {
private:
    stack<int> main, sub;
public:
    MinStack() {}
    
    void push(int val) {
        main.push(val);
        if (sub.empty() || val <= sub.top())
            sub.push(val);
    }
    
    void pop() {
        int val = main.top();
        main.pop();
        if (val == sub.top())
            sub.pop();
    }
    
    int top() {
        return main.top();
    }
    
    int getMin() {
        return sub.top();
    }
};

/**
 * Your MinStack object will be instantiated and called as such:
 * MinStack* obj = new MinStack();
 * obj->push(val);
 * obj->pop();
 * int param_3 = obj->top();
 * int param_4 = obj->getMin();
 */