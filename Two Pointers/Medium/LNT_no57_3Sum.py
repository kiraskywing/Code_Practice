# The same as LeetCode no15. 3Sum

class Solution:
    """
    @param numbers: Give an array numbers of n integer
    @return: Find all unique triplets in the array which gives the sum of zero.
    """

    def threeSum(self, numbers):
        if not numbers:
            return []

        result = []
        numbers.sort()

        for i in range(len(numbers) - 2):
            if i > 0 and numbers[i] == numbers[i - 1]:
                continue

            left, right = i + 1, len(numbers) - 1
            while left < right:
                if numbers[left] + numbers[right] > -numbers[i]:
                    right -= 1

                elif numbers[left] + numbers[right] < -numbers[i]:
                    left += 1

                else:
                    result.append([numbers[i], numbers[left], numbers[right]])
                    left += 1
                    right -= 1
                    while left < right and numbers[right] == numbers[right + 1]:
                        right -= 1
                    while left < right and numbers[left] == numbers[left - 1]:
                        left += 1

        return result

