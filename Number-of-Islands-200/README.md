###### tags: `leetcode`
# 200. Number of Islands
## DFS
Remember to add ` if not grid: return 0  # This includes None and []`
```python=
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs(grid, r, c, nr, nc):
            if r < 0 or c < 0 or c >= nc or r >= nr or grid[r][c]=='0':
                return
            grid[r][c]='0'
            dfs(grid, r-1, c  ,nr,nc)
            dfs(grid, r,   c-1,nr,nc)
            dfs(grid, r+1, c  ,nr,nc)
            dfs(grid, r,   c+1,nr,nc)
        if not grid:  # This includes None and []
            return 0
        nr = len(grid)  # number of columns
        nc = len(grid[0])  # number of rows
        ans = 0
        for r in range(nr):
            for c in range(nc):
                if grid[r][c]=='1':
                    ans+=1
                    dfs(grid,r,c,nr,nc)
        return ans
        
```
