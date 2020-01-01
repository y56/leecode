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
## BFS
```python=
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        def bfs(grid,nr,nc,q):
            
            def is_legal(r,c):
                if r<0 or c<0 or r>=nr or c>=nc or grid[r][c]=='0':
                    return False
                return True
            
            
            while q:
                (r,c) = q[0]
                grid[r][c] = '0'
                del q[0]
                if is_legal(r+1,c  ): q.append((r+1,c  ))
                if is_legal(r-1,c  ): q.append((r-1,c  ))
                if is_legal(r  ,c+1): q.append((r  ,c+1))
                if is_legal(r  ,c-1): q.append((r  ,c-1))
                    
                    
        if not grid:
            return 0
        
        nr = len(grid)
        nc = len(grid[0])
        ans = 0
        q=[]
        for r in range(nr):
            for c in range(nc):
                if grid[r][c] == '1':
                    ans+=1
                    q.append((r,c))    
                    bfs(grid,nr,nc,q)
        return ans
```
## BFS 2
```python=
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        def bfs(grid,nr,nc,q):
                        
            while q:
                (r,c) = q[0]
                grid[r][c] = '0'
                del q[0]
                if r+1>=0 and r+1<nr and grid[r+1][c]=='1': q.append((r+1,c  ))
                if r-1>=0 and r-1<nr and grid[r-1][c]=='1': q.append((r-1,c  ))
                if c+1>=0 and c+1<nc and grid[r][c+1]=='1': q.append((r  ,c+1))
                if c-1>=0 and c-1<nc and grid[r][c-1]=='1': q.append((r  ,c-1))
                    
                    
        if not grid:
            return 0
        
        nr = len(grid)
        nc = len(grid[0])
        ans = 0
        q=[]
        for r in range(nr):
            for c in range(nc):
                if grid[r][c] == '1':
                    ans+=1
                    q.append((r,c))    
                    bfs(grid,nr,nc,q)
        return ans
```