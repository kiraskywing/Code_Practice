struct Node {
    int i, j, val;
    struct Node* left;
    struct Node* right;
    Node(int i, int j) {
        this->i = i;
        this->j = j;
        left = right = nullptr;
        val = 0;
    }
};
typedef struct Node Node;

class SegTree {
private:    
    Node* build(vector<int>& nums, int i, int j) {
        if (i == j) {
            Node* cur = new Node(i, j);
            cur->val = nums[i];
            return cur;
        }

        int mid = i + (j - i) / 2;
        Node* cur = new Node(i, j);
        cur->left = build(nums, i, mid);
        cur->right = build(nums, mid + 1, j);
        cur->val = cur->left->val + cur->right->val;
        return cur;
    }

public:
    Node* root;
    
    SegTree(vector<int>& nums) {
        root = build(nums, 0, nums.size() - 1);
    }

    void update(Node* node, int idx, int val) {
        if (node->i == node->j) {
            node->val = val;
            return;
        }

        int mid = node->i + (node->j - node->i) / 2;
        if (idx <= mid)
            update(node->left, idx, val);
        else
            update(node->right, idx, val);
        node->val = node->left->val + node->right->val;
    }

    int query(Node* node, int i, int j) {
        if (node->i == i && node->j == j)
            return node->val;

        int mid = node->i + (node->j - node->i) / 2;
        if (j <= mid)
            return query(node->left, i, j);
        if (i >= mid + 1)
            return query(node->right, i, j);
        return query(node->left, i, mid) + query(node->right, mid + 1, j);
    }
};

class NumArray {
private:
    SegTree* seg;
public:
    NumArray(vector<int>& nums) {
        seg = new SegTree(nums);
    }
    
    void update(int index, int val) {
        seg->update(seg->root, index, val);
    }
    
    int sumRange(int left, int right) {
        return seg->query(seg->root, left, right);
    }
};

/**
 * Your NumArray object will be instantiated and called as such:
 * NumArray* obj = new NumArray(nums);
 * obj->update(index,val);
 * int param_2 = obj->sumRange(left,right);
 */