class Solution:
    def canMouseWin(self, grid: List[str], catJump: int, mouseJump: int) -> bool:
        m, n = len(grid), len(grid[0])
        food_pos = mouse_pos = cat_pos = None
        available = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 'F': food_pos = (i, j)
                if grid[i][j] == 'M': mouse_pos = (i, j)
                if grid[i][j] == 'C': cat_pos = (i, j)
                if grid[i][j] != '#': available += 1
        
        record = dict()
        def helper(cat_pos, mouse_pos, record, turns):
            if (cat_pos, mouse_pos, turns) in record:
                return record[(cat_pos, mouse_pos, turns)]
            if cat_pos == food_pos or cat_pos == mouse_pos or turns == available * 2:
                return False
            if mouse_pos == food_pos:
                return True
            
            curPos, curJump, curRes = (mouse_pos, mouseJump, True) if turns % 2 == 0 else (cat_pos, catJump, False)
            x, y = curPos
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                for i in range(0, curJump + 1):
                    x2, y2 = x + dx * i, y + dy * i
                    if not (0 <= x2 < m and 0 <= y2 < n) or grid[x2][y2] == '#':
                        break
                    if turns % 2 == 0 and helper(cat_pos, (x2, y2), record, turns + 1):
                        record[(cat_pos, mouse_pos, turns)] = curRes
                        return curRes
                    elif turns % 2 != 0 and not helper((x2, y2), mouse_pos, record, turns + 1):
                        record[(cat_pos, mouse_pos, turns)] = curRes
                        return curRes
            
            record[(cat_pos, mouse_pos, turns)] = not curRes
            return not curRes
        
        return helper(cat_pos, mouse_pos, record, 0)