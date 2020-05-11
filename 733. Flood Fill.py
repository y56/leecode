class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        M=len(image)
        N=len(image[0])
        c=image[sr][sc]
        if newColor==c:
            return image
        def dfs(sr,sc):
            image[sr][sc]=newColor
            if 0<=sr+1<M and 0<=sc<N and image[sr+1][sc]==c: dfs(sr+1,sc)
            if 0<=sr-1<M and 0<=sc<N and image[sr-1][sc]==c: dfs(sr-1,sc)
            if 0<=sr<M and 0<=sc+1<N and image[sr][sc+1]==c: dfs(sr,sc+1)
            if 0<=sr<M and 0<=sc-1<N and image[sr][sc-1]==c: dfs(sr,sc-1)
        dfs(sr,sc)
        return image
            
