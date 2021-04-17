class Solution {
public:
    int fib(int n) {
        int a0 = 0, a1 = 1;
        vector<vector<int>> base = {{1, 1}, {1, 0}};
        vector<vector<int>> res = {{1, 0}, {0, 1}};
        fast_power(res, base, n);
        return res[1][0] * a1 + res[1][1] * a0;
    }
    
    void fast_power(vector<vector<int>>& res, vector<vector<int>>& base, int n) {
        vector<vector<int>> temp(2, vector<int>(0, 2));
        while (n) {
            if (n & 1) {
                temp = res;
                mat_p(res, temp, base);
            }
            temp = base;
            mat_p(base, temp, temp);
            n >>= 1;
        }
    }
    
    void mat_p(vector<vector<int>>& a, vector<vector<int>>& b, vector<vector<int>>& c) {
        for (int i = 0; i < 2; i++) {
            for (int j = 0; j < 2; j++) {
                a[i][j] = 0;
                for (int k = 0; k < 2; k++)
                    a[i][j] += b[i][k] * c[k][j];
            }
        }
    }
};