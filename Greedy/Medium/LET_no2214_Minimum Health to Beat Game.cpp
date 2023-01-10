class Solution {
public:
    long long minimumHealth(vector<int>& damage, int armor) {
        int max_damage = 0;
        long total_damage = 0;

        for (int& d : damage) {
            total_damage += d;
            max_damage = max(max_damage, d);
        }

        return total_damage - min(armor, max_damage) + 1;
    }
};