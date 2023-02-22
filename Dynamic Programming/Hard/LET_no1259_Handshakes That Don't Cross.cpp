class Solution {
public:
    int numberOfWays(int numPeople) {
        const static int mod = 1'000'000'007;
        int shakes = numPeople / 2;
        vector<int> dp(shakes + 1, 0);
        dp[0] = 1;

        for (int pair = 1; pair <= shakes; pair++) {
            for (int sub_pair = 0; sub_pair < pair; sub_pair++) {
                dp[pair] += ((long long) dp[sub_pair] * dp[pair - sub_pair - 1]) % mod;
                dp[pair] %= mod;
            }
        }

        return dp[shakes];
    }
};