###### tags: `leetcode` `bfs` `dfs` `disjoint-set` `union–find` 
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
def numIslands(self, grid: List[List[str]]) -> int:    
    def bfs(grid,nr,nc,q):
        def is_legal(r,c):
            if r<0 or c<0 or r>=nr or c>=nc or grid[r][c]=='0':
            # some judgements are unnecessary for some cases
                return False
            return True

        while q:
            (r,c) = q[0]  # take the info of the head of queue
            del q[0]  # dequeue

            # we shall set a point to '0' as soon as we put it to `q`
            # otherwise, a point will appear many many times in `q`
            if is_legal(r+1,c  ): q.append((r+1,c  )); grid[r+1][c]='0'  
            if is_legal(r-1,c  ): q.append((r-1,c  )); grid[r-1][c]='0'
            if is_legal(r  ,c+1): q.append((r  ,c+1)); grid[r  ][c+1]='0'
            if is_legal(r  ,c-1): q.append((r  ,c-1)); grid[r  ][c-1]='0'

    if not grid:  # for None and []
        return 0

    nr = len(grid)
    nc = len(grid[0])
    ans = 0
    q=[]
    for r in range(nr):
        for c in range(nc):
            if grid[r][c] == '1':
                ans+=1
                q.append((r,c))  # enqueue
                grid[r][c] = '0'  # mark as visited
                bfs(grid,nr,nc,q)
    return ans
```
## BFS 2
```python=
def numIslands(self, grid: List[List[str]]) -> int:
    def bfs(grid,nr,nc,q):

        while q:
            (r,c) = q[0]
            del q[0]
            if r+1>=0 and r+1<nr and grid[r+1][c]=='1': q.append((r+1,c  )); grid[r+1][c] = '0';
            if r-1>=0 and r-1<nr and grid[r-1][c]=='1': q.append((r-1,c  )); grid[r-1][c] = '0';
            if c+1>=0 and c+1<nc and grid[r][c+1]=='1': q.append((r  ,c+1)); grid[r][c+1] = '0';
            if c-1>=0 and c-1<nc and grid[r][c-1]=='1': q.append((r  ,c-1)); grid[r][c-1] = '0';

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
                grid[r][c] = '0'
                bfs(grid,nr,nc,q)
    return ans
```
## BFS 3 WRONG
:::danger
This is wrong because `r` and `c` in `while`
:::
```python=
def numIslands(self, grid: List[List[str]]) -> int:    
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
                grid[r][c] = '0'
                while q:
                    (r,c) = q[0]  # You are changing loop counter! WRONG!
                    del q[0]
                    if r+1>=0 and r+1<nr and grid[r+1][c]=='1': q.append((r+1,c)); grid[r+1][c]='0'
                    if r-1>=0 and r-1<nr and grid[r-1][c]=='1': q.append((r-1,c)); grid[r-1][c]='0'
                    if c+1>=0 and c+1<nc and grid[r][c+1]=='1': q.append((r,c+1)); grid[r][c+1]='0'
                    if c-1>=0 and c-1<nc and grid[r][c-1]=='1': q.append((r,c-1)); grid[r][c-1]='0'
    return ans
```
## BFS 3 OK
```python=
def numIslands(grid):
    if not grid:
        return 0
    nr = len(grid)
    nc = len(grid[0])
    ans = 0
    q=[]
    for r in range(nr):
        for c in range(nc):
            if grid[r][c] == '1':
                ans += 1
                q.append((r,c))
                grid[r][c] = '0'
                while q:
                    (qr,qc) = q[0]  # in BFS-while, Use qr and qc for r and c, 
                                    # not to mess up with for-loop r and c
                    del q[0]
                    if qr+1>=0 and qr+1<nr and grid[qr+1][qc  ]=='1': q.append((qr+1,qc  )); grid[qr+1][qc  ]='0'
                    if qr-1>=0 and qr-1<nr and grid[qr-1][qc  ]=='1': q.append((qr-1,qc  )); grid[qr-1][qc  ]='0'
                    if qc+1>=0 and qc+1<nc and grid[qr  ][qc+1]=='1': q.append((qr  ,qc+1)); grid[qr  ][qc+1]='0'
                    if qc-1>=0 and qc-1<nc and grid[qr  ][qc-1]=='1': q.append((qr  ,qc-1)); grid[qr  ][qc-1]='0'
    return ans
```
## disjoint set/union-find
![](https://i.imgur.com/cF80pGi.png)
![](https://i.imgur.com/W56gEZT.png)
### my stupid functional programming QQ
:::danger
```
parent[r * nc + c] = r * nc + c  # NOT `r * nr + c`
```
:::
```python=
def numIslands(self, grid: List[List[str]]) -> int: 
    if not grid:
        return 0
    
    nr=len(grid)
    nc=len(grid[0])
    ans=0
    
    # MAKE_SET
    parent = [-1] * nc * nr
    rank = [0] * nc * nr  # height
    for r in range(nr):
        for c in range(nc):
            if grid[r][c] == '1':
                ans+=1  # every element is in its own set
                parent[r * nc + c] = r * nc + c  # NOT `r * nr + c`
    
    def FIND_SET(x, parent):
        if parent[x] != x:
            parent[x] = FIND_SET(parent[x],parent)  # path compression
            # modifying `parent` list, will be seen outside
            # path compression: let the node directly point to its root
        return parent[x]
    
    def UNION(x,y,rank,ans,parent):
        rootx = FIND_SET(x,parent)  # root of x / representative of x
        rooty = FIND_SET(y,parent)
        if rootx == rooty:  # They are in the same set
            return ans
            
        # update the data structure
        if rank[rootx] > rank[rooty]:  # to union by rank/height
            # let the shorter tree attach to the higher tree
            # so the height of the higher will not increase
            parent[rooty] = rootx      
        elif rank[rooty] > rank[rootx]:
            parent[rootx] = rooty
        else:
            parent[rooty] = rootx  # equal, wlog, let x represent for y
            rank[x] += 1  # height of x plus one
            # modifying `rank` list, will be seen outside
        
        # update the number of set
        return ans-1 
        # `ans` is not an object, modification to it will not seen outside
        # I have to return `ans` and use outside `ans` to catch it
    
    for r in range(nr):
        for c in range(nc):
            if grid[r][c] == '1':
                grid[r][c] = '0'
                here=r*nc+c
                if r+1>=0 and r+1<nr and grid[r+1][c]=='1': 
                    ans = UNION(here,(r+1)*nc+c,rank,ans,parent)
                # if r-1>=0 and r-1<nr and grid[r-1][c]=='1': 
                #     ans = UNION(here,(r-1)*nc+c,rank,ans,parent)
                if c+1>=0 and c+1<nc and grid[r][c+1]=='1': 
                    ans = UNION(here,r*nc+c+1,rank,ans,parent)
                # if c-1>=0 and c-1<nc and grid[r][c-1]=='1': 
                #     ans = UNION(here,r*nc+c-1,rank,ans,parent)
    return ans
```
## disjoint set/union-find, path compression
### my stupid functional programming
#### using python's scope mechanism to mimic global
```python=
def numIslands(self, grid: List[List[str]]) -> int: 
    if not grid:
        return 0

    nr=len(grid)
    nc=len(grid[0])
    ans=[0]  # using list, bc I want make it global

    # MAKE_SET
    parent = [-1] * nc * nr
    rank = [0] * nc * nr  # height
    for r in range(nr):
        for c in range(nc):
            if grid[r][c] == '1':
                ans[0]+=1  # every element is in its own set
                parent[r * nc + c] = r * nc + c  # NOT `r * nr + c`

    def FIND_SET(x):
        if parent[x] != x:  # This works bc python's scope design
            parent[x] = FIND_SET(parent[x])  # # path compression
            # modifying `parent` list, will be seen outside, bc of python
            # path compression: let the node directly point to its root
        return parent[x]

    def UNION(x,y):
        rootx = FIND_SET(x)  # root of x / representative of x
        rooty = FIND_SET(y)
        if rootx == rooty:  # They are in the same set
            return

        # update the data structure
        # This is python so we can access `rank` in a function
        if rank[rootx] > rank[rooty]:  # to union by rank/height
            # let the shorter tree attach to the higher tree
            # so the height of the higher will not increase
            parent[rooty] = rootx      
        elif rank[rooty] > rank[rootx]:
            parent[rootx] = rooty
        else:
            parent[rooty] = rootx  # equal, wlog, let x represent for y
            rank[x] += 1  # height of x plus one
            # modifying `rank` list, will be seen outside

        # update the number of set
        ans[0]-=1 
        # `ans` is not an object, modification to it will not seen outside
        # I have to return `ans` and use outside `ans` to catch it

    for r in range(nr):
        for c in range(nc):
            if grid[r][c] == '1':
                grid[r][c] = '0'
                here=r*nc+c
                if r+1>=0 and r+1<nr and grid[r+1][c]=='1': 
                    UNION(here,(r+1)*nc+c)
                # if r-1>=0 and r-1<nr and grid[r-1][c]=='1': 
                #     UNION(here,(r-1)*nc+c)
                if c+1>=0 and c+1<nc and grid[r][c+1]=='1': 
                    UNION(here,r*nc+c+1)
                # if c-1>=0 and c-1<nc and grid[r][c-1]=='1': 
                #     UNION(here,r*nc+c-1)
    return ans[0]
```
## disjoint set/union-find
### OOP
```python=
class disjoint_set:
    def __init__(self, grid, nr, nc):
        self.parent = [-1] * nr * nc
        self.rank = [0] * nr * nc
        self.count = 0

        i = 0
        for row in grid:
            for ele in row:
                if ele == "1":
                    self.parent[i] = i
                    self.count += 1
                i += 1
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    def union(self, x, y):
        rootx = self.find(x)
        rooty = self.find(y)
        if rootx == rooty: return 

        # to union them by ranks/heights
        if self.rank[rootx] > self.rank[rooty]:
            self.parent[rooty] = rootx
        elif self.rank[rootx] < self.rank[rooty]:
            self.parent[rootx] = rooty
        else:  # Their ranks are equal
            self.parent[rooty] = rootx  # wlog
            self.rank[rootx] += 1
        self.count -= 1
        
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int: 
        if not grid:
            return 0
        nr = len(grid)
        nc = len(grid[0])
        my_disjoint_set = disjoint_set(grid, nr, nc)
        for r in range(nr):
            for c in range(nc):
                if grid[r][c] == "1":
                    here = r * nc + c
                    if r + 1 >= 0 and r + 1 < nr and grid[r + 1][c] == '1': 
                        my_disjoint_set.union(here, (r + 1) * nc + c)
                    # if r - 1 >= 0 and r - 1 < nr and grid[r - 1][c] == '1': 
                    #     my_disjoint_set.union(here, (r - 1) * nc + c)
                    if c + 1 >= 0 and c + 1 < nc and grid[r][c + 1] == '1': 
                        my_disjoint_set.union(here, r * nc + c + 1)
                    # if c - 1 >= 0 and c - 1 < nc and grid[r][c - 1] == '1': 
                    #     my_disjoint_set.union(here, r * nc + c - 1)
                    grid[r][c] = "0"  # mark as check
        return my_disjoint_set.count
```


## from somebody else, COOL!
```python=
class Solution(object):
    def numIslands(self, grid):
        if len(grid) == 0: return 0
        row = len(grid); col = len(grid[0])
        self.count = sum(grid[i][j]=='1' for i in range(row) for j in range(col))
        parent = [i for i in range(row*col)]
        
        def find(x):
            if parent[x]!= x:
                return find(parent[x])
            return parent[x]
        
        def union(x,y):
            xroot, yroot = find(x),find(y)
            if xroot == yroot: return 
            parent[xroot] = yroot
            self.count -= 1
     
        for i in range(row):
            for j in range(col):
                if grid[i][j] == '0':
                    continue
                index = i*col + j
                if j < col-1 and grid[i][j+1] == '1':
                    union(index, index+1)
                if i < row-1 and grid[i+1][j] == '1':
                    union(index, index+col)
        return self.count
```
## >口<  SHOCK !!! We don't need to check all neighbors in disjoint-set method !!! (⊙ˍ⊙) 
:::warning
Since we are checking from left to right, from up to down,  
we only need to check the right and the down.
:::
:::danger
We have to check all four directions in BFS and DFS.
:::
## disjoint set, OOP, learn from the COOL
```python=
class disjoint_set:
    def __init__(self, grid, nr, nc):
        self.rank = [0] * nr * nc
        self.count = sum(ele == '1' for row in grid for ele in row )
        self.parent = [i for i in range(nr * nc)]  
        # it's ok for '0' to have indices, since we will not touch them
        
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    def union(self, x, y):
        rootx = self.find(x)
        rooty = self.find(y)
        if rootx == rooty: return 

        # to union them by ranks/heights
        if self.rank[rootx] > self.rank[rooty]:
            self.parent[rooty] = rootx
        elif self.rank[rootx] < self.rank[rooty]:
            self.parent[rootx] = rooty
        else:  # Their ranks are equal
            self.parent[rooty] = rootx  # wlog
            self.rank[rootx] += 1
        self.count -= 1
        
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int: 
        if not grid: return 0
        nr = len(grid)
        nc = len(grid[0])
        my_disjoint_set = disjoint_set(grid, nr, nc)
        for r in range(nr):
            for c in range(nc):
                if grid[r][c] == "1":
                    here = r * nc + c
                    if r + 1 >= 0 and r + 1 < nr and grid[r + 1][c] == '1': 
                        my_disjoint_set.union(here, (r + 1) * nc + c)
                    #if r - 1 >= 0 and r - 1 < nr and grid[r - 1][c] == '1': 
                    #    my_disjoint_set.union(here, (r - 1) * nc + c)
                    if c + 1 >= 0 and c + 1 < nc and grid[r][c + 1] == '1': 
                        my_disjoint_set.union(here, r * nc + c + 1)
                    #if c - 1 >= 0 and c - 1 < nc and grid[r][c - 1] == '1': 
                    #    my_disjoint_set.union(here, r * nc + c - 1)
                    grid[r][c] = "0"  # mark as check
        return my_disjoint_set.count
```