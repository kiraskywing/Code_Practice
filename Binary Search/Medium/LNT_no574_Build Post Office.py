class Solution:
    """
    @param grid: a 2D grid
    @return: An integer
    """

    def shortestDistance(self, grid):
        m = len(grid)
        if m == 0:
            return -1
        n = len(grid[0])
        if n == 0:
            return -1

        sum_x, sum_y, pos_x, pos_y = [0], [0], [], []

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    pos_x.append(i)
                    pos_y.append(j)
        pos_x.sort()
        pos_y.sort()
        length = len(pos_x)

        for i in range(length):
            sum_x.append(sum_x[-1] + pos_x[i])
            sum_y.append(sum_y[-1] + pos_y[i])

        result = sys.maxsize
        for i in range(pos_x[0], pos_x[-1] + 1):
            for j in range(pos_y[0], pos_y[-1] + 1):
                if grid[i][j] == 0:
                    dist_x = self.get_dist(pos_x, sum_x, i, length)
                    dist_y = self.get_dist(pos_y, sum_y, j, length)
                    if dist_x + dist_y < result:
                        result = dist_x + dist_y
        return result

    def get_dist(self, pos_rec, pos_sum, pos, length):

        if pos_rec[0] > pos:
            return pos_sum[-1] - pos * length

        left, right = 0, length - 1
        while left + 1 < right:
            mid = (left + right) // 2
            if pos_rec[mid] <= pos:
                left = mid
            else:
                right = mid

        index = 0
        if pos_rec[right] <= pos:
            index = right
        else:
            index = left

        return (pos * (index + 1) - pos_sum[index + 1]) + (pos_sum[-1] - pos_sum[index + 1]) - pos * (
                    length - (index + 1))
