class Solution:
    """
    @param nums: an integer array
    @param k: An integer
    @return: the top k largest Numbers in array
    """

    def topk(self, nums, k):
        size = len(nums)
        self.build_maxheap(nums, size)

        result = []
        for _ in range(k):
            result.append(nums[0])
            nums[0] = nums[size - 1]
            size -= 1
            self.max_heapify(nums, 0, size)
        return result

    def build_maxheap(self, nums, size):
        for i in range(size // 2 - 1, -1, -1):
            self.max_heapify(nums, i, size)

    def max_heapify(self, nums, root, size):
        while True:
            child = root * 2 + 1
            if child >= size:
                break
            if child + 1 < size and nums[child] < nums[child + 1]:
                child += 1
            if nums[root] < nums[child]:
                nums[root], nums[child] = nums[child], nums[root]
                root = child
            else:
                break