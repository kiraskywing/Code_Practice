class Solution {
public:
    int connectSticks(vector<int>& sticks) {
        int res = 0;
        priority_queue<int, vector<int>, greater<int>> min_heap(sticks.begin(), sticks.end());
        
        while (min_heap.size() > 1) {
            int a = min_heap.top();
            min_heap.pop();
            int b = min_heap.top();
            min_heap.pop();
            res += a + b;
            min_heap.push(a + b);
        }

        return res;
    }
};