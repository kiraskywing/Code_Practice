class Solution {
public:
    vector<int> dailyTemperatures(vector<int>& temperatures) {
        int n = temperatures.size();
        vector<int> res(n, 0);
        stack<int> s;
        
        for (int i = 0; i < n; i++) {
            int cur = temperatures[i];
            while (!s.empty() && temperatures[s.top()] < cur) {
                int j = s.top();
                s.pop();
                res[j] = i - j;
            }
            s.push(i);
        }
        
        return res;
    }
};