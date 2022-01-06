typedef pair<int, int> iPair;

class Solution {
public:
    bool carPooling(vector<vector<int>>& trips, int capacity) {
        auto cmp = [](iPair left, iPair right) { return left.first > right.first || left.first == right.first && left.second > right.second; };
        priority_queue<iPair, vector<iPair>, decltype(cmp)> times(cmp);
        
        for (vector<int>& trip : trips) {
            int p = trip[0], from = trip[1], to = trip[2];
            times.push(make_pair(from, p));
            times.push(make_pair(to, -p));
        }
        
        while (!times.empty()) {
            capacity -= times.top().second;
            if (capacity < 0)
                return false;
            times.pop();
        }
        return true;
    }
};