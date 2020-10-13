class Solution:
    """
    @param Numbers: An array of Integer
    @param target: target = Numbers[index1] + Numbers[index2]
    @return: [index1, index2] (index1 < index2)
    """

    def twoSum(self, numbers, target):

        temp = dict()

        for index, value in enumerate(numbers):

            if target - value not in temp:
                temp[value] = index

            else:
                return [temp[target - value], index]

        return []