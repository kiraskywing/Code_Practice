class Vector2D {
private:
    int i, j;
    vector<vector<int>> memo;
public:
    Vector2D(vector<vector<int>>& vec) {
        memo = vec;
        i = j = 0;
    }
    
    int next() {
        hasNext();
        int res = memo[i][j];
        j++;
        return res;
    }
    
    bool hasNext() {
        while (i < memo.size() && j == memo[i].size()) {
            i++;
            j = 0;
        }
        return i < memo.size();
    }
};

/**
 * Your Vector2D object will be instantiated and called as such:
 * Vector2D* obj = new Vector2D(vec);
 * int param_1 = obj->next();
 * bool param_2 = obj->hasNext();
 */