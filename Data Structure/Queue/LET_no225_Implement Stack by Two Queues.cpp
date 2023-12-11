class MyStack {
public:
    queue<int> main_q, sub_q;
    MyStack() {}
    
    void push(int x) {
        main_q.push(x);
    }
    
    int pop() {
        int n = main_q.size();
        int res;
        while (n > 1) {
            res = main_q.front();
            main_q.pop();
            sub_q.push(res);
            n--;
        }

        res = main_q.front();
        main_q.pop();
        swap(main_q, sub_q);
        return res;
    }
    
    int top() {
        int n = main_q.size();
        int res;
        while (n > 0) {
            res = main_q.front();
            main_q.pop();
            sub_q.push(res);
            n--;
        }

        swap(main_q, sub_q);
        return res;
    }
    
    bool empty() {
        return main_q.empty();
    }
};

/**
 * Your MyStack object will be instantiated and called as such:
 * MyStack* obj = new MyStack();
 * obj->push(x);
 * int param_2 = obj->pop();
 * int param_3 = obj->top();
 * bool param_4 = obj->empty();
 */