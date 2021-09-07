class Solution {
public:
    char slowestKey(vector<int>& releaseTimes, string keysPressed) {
        vector<int> times = {0};
        times.insert(times.end(), releaseTimes.begin(), releaseTimes.end());
        
        int time = 0;
        char res;
        for (int i = 1; i < times.size(); i++) {
            if (times[i] - times[i - 1] > time || times[i] - times[i - 1] == time && keysPressed[i - 1] > res) {
                time = times[i] - times[i - 1];
                res = keysPressed[i - 1];
            }
        }
        
        return res;
    }
};