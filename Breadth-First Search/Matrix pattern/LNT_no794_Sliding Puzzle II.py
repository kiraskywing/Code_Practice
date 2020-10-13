class Solution:
    """
    @param init_state: the initial state of chessboard
    @param final_state: the final state of chessboard
    @return: return an integer, denote the number of minimum moving
    """

    def minMoveStep(self, init_state, final_state):
        if str(init_state) == str(final_state):
            return 0

        final = str(final_state)
        m, n = len(init_state), len(init_state[0])
        for x in range(m):
            for y in range(n):
                if init_state[x][y] == 0:
                    X, Y = x, y

        bfs = [[init_state, X, Y, 0]]
        seen = {str(init_state)}
        shift = [(1, 0), (0, 1), (-1, 0), (0, -1)]

        for arr, x, y, steps in bfs:

            for (dx, dy) in shift:
                x2, y2 = x + dx, y + dy
                if 0 <= x2 < m and 0 <= y2 < n:
                    arr[x2][y2], arr[x][y] = arr[x][y], arr[x2][y2]

                    new_arr = str(arr)
                    if new_arr not in seen:
                        if new_arr == final:
                            return steps + 1

                        seen.add(new_arr)
                        bfs.append([[row[:] for row in arr], x2, y2, steps + 1])

                    arr[x2][y2], arr[x][y] = arr[x][y], arr[x2][y2]

        return -1