"""
54. Spiral Matrix
Medium

Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in spiral order.

Example 1:

Input:
[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
Output: [1,2,3,6,9,8,7,4,5]

Example 2:

Input:
[
  [1, 2, 3, 4],
  [5, 6, 7, 8],
  [9,10,11,12]
]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]
"""
"""
40 min
time:n
space:n
"""
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m=len(matrix)
        if m==0: return []
        n=len(matrix[0])
        if n==0: return []
        memory=set()
        def next_index(i,j,direction):
            if direction=='u':return i-1,j
            if direction=='d':return i+1,j
            if direction=='l':return i,j-1
            if direction=='r':return i,j+1
        def next_direction(direction):
            if direction=='u':return 'r'
            if direction=='d':return 'l'
            if direction=='l':return 'u'
            if direction=='r':return 'd'
        def bad(ii,jj):
            if (ii,jj) in memory:return True
            if not (0 <= ii < m):return True
            if not (0 <= jj < n):return True
            return False
        i,j=0,0
        direction='r'
        ans=[]
        for k in range(n*m):
            memory.add((i,j))
            # print(i,j,direction)
            ans.append(matrix[i][j])
            ii,jj=next_index(i,j,direction)
            if bad(ii,jj):
                direction = next_direction(direction)
                # print(direction,i,j,direction)
                ii,jj=next_index(i,j,direction)
            i,j=ii,jj
        return ans
"""
time: n
space: 1
"""
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m=len(matrix)
        if m==0: return []
        n=len(matrix[0])
        if n==0: return []
        self.up_bound  = -1
        self.down_bound = m
        self.left_bound = -1
        self.right_bound= n
        def next_index(i,j,direction):
            if direction=='u':return i-1,j
            if direction=='d':return i+1,j
            if direction=='l':return i,j-1
            if direction=='r':return i,j+1
        def next_direction(direction):
            if direction=='u':return 'r'
            if direction=='d':return 'l'
            if direction=='l':return 'u'
            if direction=='r':return 'd'
        def bad(ii,jj):
            if not (self.up_bound < ii < self.down_bound):return True
            if not (self.left_bound < jj < self.right_bound):return True
            return False
        def update_bound(direction):
            if direction=='u':self.left_bound+=1
            if direction=='d':self.right_bound-=1
            if direction=='l':self.down_bound-=1
            if direction=='r':self.up_bound+=1
            
        i,j=0,0
        direction='r'
        ans=[]
        for k in range(n*m):
            ans.append(matrix[i][j])
            ii,jj=next_index(i,j,direction)
            if bad(ii,jj):
                update_bound(direction)
                direction = next_direction(direction)
                ii,jj=next_index(i,j,direction)
            i,j=ii,jj
        return ans
