class Solution:
    def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:
        # wall: meet '1' or the maze boundary
        # will the ball start at wall? => No
        
        # Approach: dfs with memoization:
        # To memo: stop points
        # use a helper function, start point (i, j) and destination as input
        #   if (i, j) is the destination, return true
        #   otherwise choose a direction and go straight until meeting the wall or boundary
        #   do next recursive search
        #   if no result, return false
        
        return self.dfs(maze, start[0], start[1], destination[0], destination[1], dict())
    
    def dfs(self, maze, i, j, dest_i, dest_j, memo):
        # Time: O(n), Space: O(n); where n is the number of total cells
        if (i, j) == (dest_i, dest_j):
            return True
        
        m, n = len(maze), len(maze[0])
        
        if (i, j) not in memo:
            memo[(i, j)] = False
            for di, dj in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                i2, j2 = i, j
                while 0 <= i2 + di < m and 0 <= j2 + dj < n and maze[i2 + di][j2 + dj] == 0:
                    i2 += di
                    j2 += dj
                
                if self.dfs(maze, i2, j2, dest_i, dest_j, memo):
                    memo[(i, j)] = True
                    break
        
        return memo[(i, j)]