class UnionFind {
private:
    vector<int> parent;

public:
    UnionFind(int n) {
        for (int i = 0; i < n; i++)
            parent.emplace_back(i);
    }
    
    int find(int i) {
        if (parent[i] != i)
            parent[i] = find(parent[i]);
        return parent[i];
    }
    
    pair<int, int> uni(int i, int j) {
        int pi = find(i);
        int pj = find(j);
        parent[pi] = pj;
        return pair<int, int>(pi, pj);
    }
};

class Solution {
public:
    vector<vector<int>> matrixRankTransform(vector<vector<int>>& matrix) {
        map<int, vector<pair<int, int>>> record;
        int m = matrix.size();
        int n = matrix[0].size();
        vector<int> ranks(m + n);
        
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++)
                record[matrix[i][j]].emplace_back(pair<int, int>(i, j));
        }
        
        for (auto& [k, v] : record) {
            vector<int> ranks2 = ranks;
            UnionFind uf(m + n);
            
            for (auto& [i, j] : v) {
                auto pos = uf.uni(i, m + j);
                ranks2[pos.second] = max(ranks2[pos.first], ranks2[pos.second]);
            }
            
            for (auto& [i, j] : v) {
                ranks[i] = ranks[m + j] = matrix[i][j] = ranks2[uf.find(i)] + 1;
            }
        }
        
        return matrix;
    }
};