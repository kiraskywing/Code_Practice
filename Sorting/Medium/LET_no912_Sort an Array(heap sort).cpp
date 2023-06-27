class Solution {
private:
    int n;
public:
    vector<int> sortArray(vector<int>& nums) {
        n = nums.size();
        buildMaxHeap(nums);
        sortHelper(nums);
        return nums;
    }

    void buildMaxHeap(vector<int>& nums) {
        for (int i = n / 2 - 1; i >= 0; i--)
            maxHeapify(nums, i);
    }

    void maxHeapify(vector<int>& nums, int parent) {
        while (true) {
            int child = parent * 2 + 1;
            if (child >= n)
                break;
            
            if (child + 1 < n && nums[child + 1] > nums[child])
                child++;
            if (nums[child] > nums[parent]) {
                swap(nums[child], nums[parent]);
                parent = child;
            }
            else
                break;
        }
    }

    void sortHelper(vector<int>& nums) {
        for (int i = n - 1; i >= 0; i--) {
            swap(nums[0], nums[i]);
            n--;
            maxHeapify(nums, 0);
        }
    }
};