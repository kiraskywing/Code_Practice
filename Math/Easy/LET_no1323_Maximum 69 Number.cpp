class Solution {
public:
    int maximum69Number (int num) {
        int pos = 0, res_i = -1;
        int temp = num;
        
        while (temp > 0) {
            if (temp % 10 == 6)
                res_i = pos;
            
            temp /= 10;
            pos++;
        }
        
        return (res_i == -1 ? num : num + 3 * pow(10, res_i));
    }
};