class ZigzagIterator {
private:
    vector<int> v1, v2;
    queue<pair<int, int>> q;
public:
    ZigzagIterator(vector<int>& v1, vector<int>& v2) {
        if (!v1.empty()) {
            this->v1 = v1;
            q.push({0, 0});
        }
        if (!v2.empty()) {
            this->v2 = v2;
            q.push({1, 0});
        }
    }

    int next() {
        auto cur = q.front();
        q.pop();
        int res;
        if (cur.first == 0) {
            int i = cur.second;
            res = v1[i];
            if (i + 1 < v1.size())
                q.push({0, i + 1});
        }
        if (cur.first == 1) {
            int i = cur.second;
            res = v2[i];
            if (i + 1 < v2.size())
                q.push({1, i + 1});
        }
        return res;
    }

    bool hasNext() {
        return !q.empty();
    }
};

/**
 * Your ZigzagIterator object will be instantiated and called as such:
 * ZigzagIterator i(v1, v2);
 * while (i.hasNext()) cout << i.next();
 */