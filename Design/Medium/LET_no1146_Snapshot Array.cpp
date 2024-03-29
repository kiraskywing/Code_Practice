class SnapshotArray {
private:
    int snap_id;
    vector<map<int,int>> memo;
public:
    SnapshotArray(int length) {
        snap_id = 0;
        for (int i = 0; i < length; i++) {
            map<int, int> entry;
            entry[0] = 0;
            memo.push_back(entry);
        }
    }
    
    void set(int index, int val) {
        memo[index][snap_id] = val;
    }
    
    int snap() {
        return snap_id++;
    }
    
    int get(int index, int snap_id) {
        auto it = memo[index].upper_bound(snap_id);
        it--;
        return it->second;
    }
};

/**
 * Your SnapshotArray object will be instantiated and called as such:
 * SnapshotArray* obj = new SnapshotArray(length);
 * obj->set(index,val);
 * int param_2 = obj->snap();
 * int param_3 = obj->get(index,snap_id);
 */