class MyQueue {
public:
    stack<int> main_s, sub_s;
    MyQueue() {}
    
    void push(int x) {
        main_s.push(x);
    }
    
    int pop() {
        int n = main_s.size();
        while (n-- > 1) {
            int num = main_s.top();
            main_s.pop();
            sub_s.push(num);
        }

        int res = main_s.top();
        main_s.pop();
        while (!sub_s.empty()) {
            int num = sub_s.top();
            sub_s.pop();
            main_s.push(num);
        }

        return res;
    }
    
    int peek() {
        int res;
        while (!main_s.empty()) {
            res = main_s.top();
            main_s.pop();
            sub_s.push(res);
        }

        while (!sub_s.empty()) {
            int num = sub_s.top();
            sub_s.pop();
            main_s.push(num);
        }

        return res;
    }
    
    bool empty() {
        return main_s.empty();
    }
};

/**
 * Your MyQueue object will be instantiated and called as such:
 * MyQueue* obj = new MyQueue();
 * obj->push(x);
 * int param_2 = obj->pop();
 * int param_3 = obj->peek();
 * bool param_4 = obj->empty();
 */