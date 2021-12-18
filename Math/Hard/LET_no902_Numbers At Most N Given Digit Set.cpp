class Solution {
public:
    int atMostNGivenDigitSet(vector<string>& digits, int n) {
        string target = to_string(n);
        int tSize = target.size(), dSize = digits.size(), res = 0;
        
        for (int i = 1; i < tSize; i++)
            res += pow(dSize, i);
        
        for (int i = 0; i < tSize; i++) {
            bool hasSame = false;
            for (string& d : digits) {
                if (d[0] < target[i])
                    res += pow(dSize, tSize - i - 1);
                else if (d[0] == target[i])
                    hasSame = true;
            }
            if (!hasSame)
                return res;
        }
        
        return res + 1;
    }
};