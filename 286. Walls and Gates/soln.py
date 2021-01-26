class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        q = [(i, j) 
             for i,row in enumerate(rooms) 
             for j,x in enumerate(row) 
             if x==0] # find those gates and add them to queue
        
        for i, j in q:
            for ii, jj in (i+1, j), (i-1, j), (i, j+1), (i, j-1):
                if 0 <= ii < len(rooms) \
                and 0 <= jj < len(rooms[0]) \
                and rooms[ii][jj] == 2147483647:
                    rooms[ii][jj] = rooms[i][j] + 1
                    q.append((ii, jj))
class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        q = [(i, j) 
             for i,row in enumerate(rooms) 
             for j,x in enumerate(row) 
             if x==0] # find those gates and add them to queue
        
        while q:
            i,j=q[0]
            del q[0]
            for ii, jj in (i+1, j), (i-1, j), (i, j+1), (i, j-1):
                if 0 <= ii < len(rooms) \
                and 0 <= jj < len(rooms[0]) \
                and rooms[ii][jj] == 2147483647:
                    rooms[ii][jj] = rooms[i][j] + 1
                    q.append((ii, jj))
class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        q = deque((i, j) 
             for i,row in enumerate(rooms) 
             for j,x in enumerate(row) 
             if x==0) # find those gates and add them to queue
        
        while q:
            i,j=q.popleft()
            for ii, jj in (i+1, j), (i-1, j), (i, j+1), (i, j-1):
                if 0 <= ii < len(rooms) \
                and 0 <= jj < len(rooms[0]) \
                and rooms[ii][jj] == 2147483647:
                    rooms[ii][jj] = rooms[i][j] + 1
                    q.append((ii, jj))
