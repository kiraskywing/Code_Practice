class Solution:
    """
    @param num: an integer
    @return: whether the integer is a power of 4
    """
    def is_power_of_four(self, num: int) -> bool:
        if num == 1:
            return True
        if num < 0:
		    return False
        if num % 10 not in (4, 6):
            return False
        return num & (num - 1) == 0
