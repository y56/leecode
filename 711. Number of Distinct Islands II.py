class Solution:
    def numDistinctIslands2(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]: return 0
        M,N=len(grid),len(grid[0])
        seen=set()
        def dfs_explore(r,c,li_of_island_coord):
            if (    0 <= r < M 
                and 0 <= c < N 
                and grid[r][c]==1 
                and (r, c) not in seen):
                seen.add((r, c))
                li_of_island_coord.append((r, c))
                dfs_explore(r+1, c,li_of_island_coord)
                dfs_explore(r-1, c,li_of_island_coord)
                dfs_explore(r, c+1,li_of_island_coord)
                dfs_explore(r, c-1,li_of_island_coord)
        def translated(li_of_island_coord):
            # use leftup corner of the outer square as the new (0,0) of the new reference frame
            # and do translational shift
            up_r=min(r for r,c in li_of_island_coord)
            left_c=min(c for r,c in li_of_island_coord)
            return frozenset((r-up_r,c-left_c)
                             for r,c in li_of_island_coord)
        def anticlock_90_rotated(pattern,up_r,down_r,left_c,right_c):
            return frozenset((-c+(right_c-left_c),r)
                             for r,c in pattern),left_c,right_c,up_r,down_r
        def horizontally_mirrored(pattern,up_r,down_r,left_c,right_c):
            return frozenset((r,-c+(right_c-left_c)) for r,c in pattern)
        def all_patterns(pattern):
            output=[]
            up_r,   down_r  = 0, max(r for r,c in pattern)
            left_c, right_c = 0, max(c for r,c in pattern)
            
            output.append(pattern) # before anticlock_rotate90
            
            # the mirrored, before anticlock_rotate90 
            output.append(horizontally_mirrored(pattern,up_r,down_r,left_c,right_c)) 
            
            for _ in range(3):
                pattern,up_r,down_r,left_c,right_c = \
                anticlock_90_rotated(pattern,up_r,down_r,left_c,right_c)
                output.append(pattern) 
                output.append(horizontally_mirrored(pattern,up_r,down_r,left_c,right_c))
                
            return output # 8 kinds of patterns
            
        ans=0
        li_of_island_coord=[]
        pattern_pool=set()
        for r,row in enumerate(grid):
            for c,ele in enumerate(row):
                li_of_island_coord.clear()
                dfs_explore(r,c,li_of_island_coord)
                
                if not li_of_island_coord:
                    continue

                pattern=translated(li_of_island_coord)
                if pattern not in pattern_pool:
                    ans+=1
                    pattern_pool.update(all_patterns(pattern))
        return ans
