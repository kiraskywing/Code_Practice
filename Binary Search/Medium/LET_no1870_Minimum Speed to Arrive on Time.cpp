class Solution {
private:
    int n;
public:
    int minSpeedOnTime(vector<int>& dist, double hour) {
        n = dist.size();
        if (hour <= double(n - 1))
            return -1;

        int low = 1, high = 1e7;
        while (low + 1 < high) {
            int mid = low + (high - low) / 2;
            if (reachable(dist, mid, hour))
                high = mid;
            else
                low = mid;
        }

        return reachable(dist, low, hour) ? low : high;
    }

    bool reachable(vector<int>& dist, int speed, double target) {
        double time = 0.0;
        for (int i = 0; i < n - 1; i++)
            time += (dist[i] + speed - 1) / speed;

        time += double(dist[n - 1]) / speed;
        
        return time <= target;
    }
};