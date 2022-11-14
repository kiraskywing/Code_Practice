class UnionFind {
private:
    unordered_map<int, int> parent;
    int groups;
public:
    UnionFind(vector<vector<int>>& points) {
        for (int i = 0; i < points.size(); i++) {
            int x = points[i][0], y = points[i][1];
            parent[x] = x;
            parent[~y] = ~y;
        }
        groups = parent.size();
    }
    
    int find(int x) {
        int root = x;
        while (root != parent[root])
            root = parent[root];
        
        while (x != parent[x]) {
            int temp = parent[x];
            parent[x] = root;
            x = temp;
        }
        
        return root;
    }
    
    void Union(int x, int y) {
        int px = find(x), py = find(y);
        if (px != py) {
            groups--;
            parent[px] = py;
        }
    }
    
    int getGroupSize(void) { return groups; }
};

class Solution {
public:
    int removeStones(vector<vector<int>>& stones) {
        UnionFind uf = UnionFind(stones);
        for (int i = 0; i < stones.size(); i++) {
            int x = stones[i][0], y = stones[i][1];
            uf.Union(x, ~y);
        }
        
        return stones.size() - uf.getGroupSize();
    }
};