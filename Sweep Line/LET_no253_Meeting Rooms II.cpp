class Solution {
public:
    int minMeetingRooms(vector<vector<int>>& intervals) {
        map<int, int> time_uses;
        for (auto& itv : intervals) {
            time_uses[itv[0]]++;
            time_uses[itv[1]]--;
        }

        int cur = 0, res = 0;
        for (auto& it : time_uses) {
            cur += it.second;
            res = max(res, cur);
        }

        return res;
    }
};