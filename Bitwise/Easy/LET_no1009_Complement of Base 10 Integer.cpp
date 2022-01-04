class Solution {
public:
    int bitwiseComplement(int n) {
        int res = 1;
        while (res < n)
            res = (res << 1) + 1;
        return res ^ n;
    }
};