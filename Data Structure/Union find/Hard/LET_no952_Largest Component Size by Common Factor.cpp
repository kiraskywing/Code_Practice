class unionFind {
private:
    vector<int>parent, size, rank;
public:
    unionFind(vector<int>& arr, int n) {
        parent.resize(n);
        size.resize(n);
        rank.resize(n);
        for (int i = 0; i < n; i++)
            parent[i] = i;
        for (int num : arr)
            size[num] = 1;
    }
    
    int find(int x) {
        if (parent[x] != x)
            parent[x] = find(parent[x]);
        return parent[x];
    }
    
    void Union(int x, int y) {
        int px = find(x), py = find(y);
        if (px != py) {
            if (rank[px] < rank[py]) {
                parent[px] = py;
                size[py] += size[px];
                size[px] = 0;
            }
            else {
                parent[py] = px;
                size[px] += size[py];
                size[py] = 0;
                rank[px] += rank[px] == rank[py];
            }
        }
    }
    
    int largestComponentSize() {
        return *max_element(size.begin(), size.end());
    }
};

class Solution {
public:
    int largestComponentSize(vector<int>& nums) {
        int n = nums.size(), mx = *max_element(nums.begin(), nums.end());
        unionFind uf(nums, mx + 1);
        
        for (int num : nums) {
            for (int i = 2; i * i <= num; i++) {
                if (num % i == 0) {
                    uf.Union(num / i, num);
                    uf.Union(i, num);
                }
            }
        }
        
        return uf.largestComponentSize();
    }
};