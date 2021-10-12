/** 
 * Forward declaration of guess API.
 * @param  num   your guess
 * @return 	     -1 if num is lower than the guess number
 *			      1 if num is higher than the guess number
 *               otherwise return 0
 * int guess(int num);
 */

class Solution {
public:
    int guessNumber(int n) {
        long left = 1, right = n;
        while (left + 1 < right) {
            int mid = (left + right) / 2;
            if (guess(mid) == -1)
                right = mid;
            else
                left = mid;
            
        }
        if (guess(left) == 0)
            return left;
        return right;
    }
};