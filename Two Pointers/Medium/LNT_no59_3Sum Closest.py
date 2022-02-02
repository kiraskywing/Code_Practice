# The same as LeetCode no16. 3Sum Closest

class Solution:
    """
    @param Numbers: Give an array Numbers of n integer
    @param target: An integer
    @return: return the sum of the three integers, the sum closest target.
    """

    def threeSumClosest(self, numbers, target):
        numbers.sort()
        ans = sys.maxsize
        for i in range(len(numbers)):
            left, right = i + 1, len(numbers) - 1
            while left < right:
                val = numbers[left] + numbers[right] + numbers[i]
                if abs(val - target) < abs(ans - target):
                    ans = val

                if val > target:
                    right -= 1
                else:
                    left += 1

        return ans
