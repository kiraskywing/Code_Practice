class Solution:
    def rectangleArea(self, rectangles: List[List[int]]) -> int:
        xs, ys = [], []
        for x1, y1, x2, y2 in rectangles:
            xs.extend([x1, x2])
            ys.extend([y1, y2])
            
        xs = sorted(set(xs))
        ys = sorted(set(ys))
        x_i = {x : i for i, x in enumerate(xs)}
        i_x = {i : x for i, x in enumerate(xs)}
        y_j = {y : j for j, y in enumerate(ys)}
        j_y = {j : y for j, y in enumerate(ys)}
        
        board = [[0] * len(ys) for _ in range(len(xs))]
        for x1, y1, x2, y2 in rectangles:
            i1, i2, j1, j2 = x_i[x1], x_i[x2], y_j[y1], y_j[y2]
            for i in range(i1, i2):
                for j in range(j1, j2):
                    board[i][j] = 1
                    
        res, mod = 0, 10 ** 9 + 7
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == 1:
                    res += (i_x[i + 1] - i_x[i]) * (j_y[j + 1] - j_y[j])
                    res %= mod
        
        return res