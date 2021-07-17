# The same as LeetCode no18. 4Sum

class Solution:
    """
    @param Numbers: Give an array
    @param target: An integer
    @return: Find all unique quadruplets in the array which gives the sum of zero
    """

    def fourSum(self, numbers, target):
        numbers.sort()
        result = []

        for i in range(len(numbers) - 3):
            if i > 0 and numbers[i] == numbers[i - 1]:
                continue
            for j in range(i + 1, len(numbers) - 2):
                if j > i + 1 and numbers[j] == numbers[j - 1]:
                    continue
                rest = target - numbers[i] - numbers[j]
                left, right = j + 1, len(numbers) - 1

                while left < right:
                    value = numbers[left] + numbers[right]
                    if value == rest:
                        result.append([numbers[i], numbers[j], numbers[left], numbers[right]])
                        left += 1
                        right -= 1
                        while left < right and numbers[left] == numbers[left - 1]:
                            left += 1
                        while left < right and numbers[right] == numbers[right + 1]:
                            right -= 1

                    elif value > rest:
                        right -= 1
                        while left < right and numbers[right] == numbers[right + 1]:
                            right -= 1

                    else:
                        left += 1
                        while left < right and numbers[left] == numbers[left - 1]:
                            left += 1

        return result
