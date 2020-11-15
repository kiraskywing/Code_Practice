class TwoSum:

    def __init__(self):
        self.record = dict()

    """
    @param number: An integer
    @return: nothing
    """

    def add(self, number):

        if number not in self.record:
            self.record[number] = 1
        else:
            self.record[number] += 1

    """
    @param value: An integer
    @return: Find if there exists any pair of Numbers which sum is equal to the value.
    """

    def find(self, value):

        for num in self.record:
            if value - num in self.record and (value - num != num or self.record[num] > 1):
                return True

        return False