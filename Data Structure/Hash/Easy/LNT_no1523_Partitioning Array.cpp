class Solution {
public:
    /**
     * @param A: Integer array
     * @param k: a integer
     * @return: return is possible to partition the array satisfying the above conditions
     */
    bool PartitioningArray(vector<int> &A, int k) {
        // write your code here
        if (A.size() % k != 0)
            return false;
        
        unordered_map<int, int> record;
        for (int num : A)
            record[num]++;
        
        int groups = A.size() / k;
        for (auto& it : record) {
            if (it.second > groups)
                return false;
        }
        return true;
    }
};