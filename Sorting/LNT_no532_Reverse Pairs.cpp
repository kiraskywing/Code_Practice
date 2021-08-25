class Solution {
public:
    /**
     * @param A: an array
     * @return: total of reverse pairs
     */
    long long reversePairs(vector<int> &nums) {
        int n = nums.size();
        if (n < 2)
            return 0;
        
        vector<int> temp(n, 0);
        return mergeSort(nums, temp, 0, n - 1);
    }

    long long mergeSort(vector<int>& nums, vector<int>& temp, int left, int right) {
        if (left >= right)
            return 0;
        
        int mid = (left + right) / 2;
        long long res = 0;
        res += mergeSort(nums, temp, left, mid);
        res += mergeSort(nums, temp, mid + 1, right);
        res += merger(nums, temp, left, right);
        
        return res;
    }
    
    long long merger(vector<int>& nums, vector<int>& temp, int left, int right) {
        int mid = (left + right) / 2;
        int i = left, j = mid + 1, index = left;
        long long res = 0;
        
        while (i <= mid && j <= right) {
            if (nums[i] > nums[j]) {
                temp[index] = nums[j];
                j++;
                res += mid - i + 1;
            }
            else {
                temp[index] = nums[i];
                i++;
            }
            index++;
        }
        while (i <= mid) {
            temp[index] = nums[i];
            i++;
            index++;
        }
        while (j <= right) {
            temp[index] = nums[j];
            j++;
            index++;
        }
        
        for (index = left; index <= right; index++)
            nums[index] = temp[index];
        
        return res;
    }
};