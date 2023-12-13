class UnionFind {
private:
    vector<int> parents, sizes;
public:
    UnionFind(int n) {
        sizes.resize(n, 1);
        parents.resize(n);
        for (int i = 0; i < n; i++)
            parents[i] = i;
    }

    int find(int i) {
        if (parents[i] != i)
            parents[i] = find(parents[i]);
        return parents[i];
    }

    void join(int i, int j) {
        int pi = find(i), pj = find(j);
        if (pi != pj) {
            parents[pj] = pi;
            sizes[pi] += sizes[pj];
        }
    }

    int getMax() {
        int res = 0;
        for (int size : sizes)
            res = max(res, size);
        return res;
    }
};

class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        int n = nums.size();
        if (n == 0)
            return 0;

        UnionFind uf(n);
        unordered_map<int, int> memo;
        for (int i = 0; i < n; i++) {
            int num = nums[i];
            if (memo.count(num))
                continue;

            if (memo.count(num + 1)) {
                uf.join(i, memo[num + 1]);
            }
            if (memo.count(num - 1)) {
                uf.join(i, memo[num - 1]);
            }
            
            memo[num] = i;
        }

        return uf.getMax();
    }
};