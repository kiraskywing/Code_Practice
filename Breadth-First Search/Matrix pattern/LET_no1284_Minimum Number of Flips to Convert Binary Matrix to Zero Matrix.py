class Solution:
    def minFlips(self, mat: List[List[int]]) -> int:
        if all(any(r) == False for r in mat):
            return 0

        m, n = len(mat), len(mat[0])
        bfs = [[mat, 0]]
        seen = {str(mat)}

        for arr, steps in bfs:
            for i in range(m):
                for j in range(n):

                    self.flip_neighbors(arr, i, j)
                    if all(any(r) == False for r in arr):
                        return steps + 1

                    new_arr = str(arr)
                    if new_arr not in seen:
                        seen.add(new_arr)
                        bfs.append([[row[:] for row in arr], steps + 1])
                    self.flip_neighbors(arr, i, j)

        return -1

    def flip_neighbors(self, arr, x, y):
        for dx, dy in [[0, 1], [1, 0], [-1, 0], [0, -1], [0, 0]]:
            x2, y2 = x + dx, y + dy
            if 0 <= x2 < len(arr) and 0 <= y2 < len(arr[0]):
                arr[x2][y2] ^= 1
