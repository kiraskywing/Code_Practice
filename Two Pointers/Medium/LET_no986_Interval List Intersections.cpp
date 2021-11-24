class Solution {
public:
    vector<vector<int>> intervalIntersection(vector<vector<int>>& firstList, vector<vector<int>>& secondList) {
        vector<vector<int>> res;
        int n1 = firstList.size(), n2 = secondList.size(), i = 0, j = 0;
        while (i < n1 && j < n2) {
            auto& first = firstList[i];
            auto& second = secondList[j];
            if (first[0] <= second[1] && second[0] <= first[1])
                res.push_back({max(first[0], second[0]), min(first[1], second[1])});
            if (first[1] <= second[1])
                i++;
            else
                j++;
        }
        
        return res;
    }
};