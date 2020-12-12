class Solution:
    def numOfBurgers(self, tomatoSlices: int, cheeseSlices: int) -> List[int]:
        if tomatoSlices == 0 and cheeseSlices == 0:
            return [0, 0]
        if tomatoSlices % 2 != 0:
            return []

        double_jumbo = (tomatoSlices - cheeseSlices * 2)
        if double_jumbo < 0 or double_jumbo % 2 != 0:
            return []
        jumbo = double_jumbo // 2
        small = cheeseSlices - jumbo
        if small < 0:
            return []

        return [jumbo, small]