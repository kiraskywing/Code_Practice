class Solution {
public:
    int shipWithinDays(vector<int>& weights, int days) {
        int min_cap = *max_element(weights.begin(), weights.end());
        int max_cap = accumulate(weights.begin(), weights.end(), 0);

        while (min_cap + 1 < max_cap) {
            int cap = min_cap + (max_cap - min_cap) / 2;
            cout << cap << endl;
            int count_days = counter(weights, cap);
            if (count_days > days)
                min_cap = cap;
            else
                max_cap = cap;
        }

        if (counter(weights, min_cap) <= days)
            return min_cap;
        return max_cap;
    }

    int counter(vector<int>& weights, int limit) {
        int res = 0, cur_cap = 0;
        for (int w : weights) {
            if (cur_cap + w > limit) {
                res++;
                cur_cap = 0;
            }
            cur_cap += w;
        }

        return res + 1;
    }
};