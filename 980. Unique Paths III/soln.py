class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        # step 1). initialize the conditions for backtracking
        #   i.e. initial state and final state
        rows, cols = len(grid), len(grid[0])
        non_obstacles = 0
        start_row, start_col = 0, 0
        for i,r in enumerate(grid):
            for j,x in enumerate(r):
                if  x >= 0:
                    non_obstacles += 1
                if x == 1:
                    start_row, start_col = i, j

        # count of paths as the final result
        path_count = 0

        # step 2). backtrack on the grid
        def backtrack(row, col, remain):
            # we need to modify this external variable
            nonlocal path_count

            # base case for the termination of backtracking
            if grid[row][col] == 2 and remain == 1:
                # reach the destination
                path_count += 1
                return

            # mark the square as visited. case: 0, 1, 2 
            temp = grid[row][col] # remember the original
            grid[row][col] = -4 # mark as visited
            

            # explore the 4 potential directions around
            for ro, co in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                next_row, next_col = row + ro, col + co

                if not (0 <= next_row < rows and 0 <= next_col < cols):
                    # invalid coordinate
                    continue
                if grid[next_row][next_col] < 0:
                    # either obstacle or visited square
                    continue

                backtrack(next_row, next_col, remain-1)
                # we now have one less square to visit

            # unmark the square after the visit
            grid[row][col] = temp

        backtrack(start_row, start_col, non_obstacles)

        return path_count
    
    
class Solution:
    def uniquePathsIII(self, A):
        self.res = 0
        m, n, empty = len(A), len(A[0]), 1
        for i in range(m):
            for j in range(n):
                if A[i][j] == 1:
                    x, y = (i, j)
                elif A[i][j] == 0:
                    empty += 1

        def dfs(x, y, empty):
            if not (0 <= x < m and 0 <= y < n and A[x][y] >= 0): return
            if A[x][y] == 2:
                self.res += empty == 0
                return
            A[x][y] = -2
            dfs(x + 1, y, empty - 1)
            dfs(x - 1, y, empty - 1)
            dfs(x, y + 1, empty - 1)
            dfs(x, y - 1, empty - 1)
            A[x][y] = 0
        dfs(x, y, empty)
        return self.res
