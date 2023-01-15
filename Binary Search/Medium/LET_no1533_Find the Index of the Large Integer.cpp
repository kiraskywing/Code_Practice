/**
 * // This is the ArrayReader's API interface.
 * // You should not implement it, or speculate about its implementation
 * class ArrayReader {
 *   public:
 *     // Compares the sum of arr[l..r] with the sum of arr[x..y] 
 *     // return 1 if sum(arr[l..r]) > sum(arr[x..y])
 *     // return 0 if sum(arr[l..r]) == sum(arr[x..y])
 *     // return -1 if sum(arr[l..r]) < sum(arr[x..y])
 *     int compareSub(int l, int r, int x, int y);
 *
 *     // Returns the length of the array
 *     int length();
 * };
 */

class Solution {
public:
    int getIndex(ArrayReader &reader) {
        int left = 0, right = reader.length() - 1;
        
        while (left + 1 < right) {
            int mid = (left + right) / 2;
            int is_even = (right - left + 1) % 2 == 0;
            if (reader.compareSub(left, mid, mid + is_even, right) == 1)
                right = mid;
            else
                left = mid;
        }

        if (reader.compareSub(left, left, right, right) == 1)
            return left;
        return right;
    }
};