class Solution:
    """
    @param colors: A list of integer
    @param k: An integer
    @return: nothing
    """

    def sortColors2(self, colors, k):

        self.helper(colors, 0, len(colors) - 1, 1, k)

    def helper(self, colors, left, right, c_from, c_to):

        if left >= right or c_from >= c_to:
            return

        i, j = left, right

        color = (c_from + c_to) // 2

        while i <= j:

            while i <= j and colors[i] <= color:
                i += 1

            while i <= j and color < colors[j]:
                j -= 1

            if i <= j:
                colors[i], colors[j] = colors[j], colors[i]
                i += 1
                j -= 1

        self.helper(colors, left, j, c_from, color)
        self.helper(colors, i, right, color + 1, c_to)