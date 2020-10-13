class Solution:
    """
    @param nums: An integer array
    @return: The second max number in the array.
    """
    def secondMax(self, nums):

        nums.sort(reverse=True)
        i = nums[0]
        for j in range(1, len(nums)):
            if nums[j] <= i:  # 真的判斷第二大不該有等號
                return nums[j]
        return i

        """
        f_value = max(nums[0], nums[1])
        s_value = min(nums[0], nums[1])
        if len(nums) < 3:
            return s_value
        else:
            for i in range(2, len(nums)):
                if nums[i] > f_value:
                    s_value = f_value
                    f_value = nums[i]
                elif nums[i] > s_value:
                    s_value = nums[i]
            return s_value
        """