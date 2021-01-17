" bad "
class Solution:
    def oddCells(self, n: int, m: int, indices: List[List[int]]) -> int:
        A=[[0]*m for _ in range(n)]
        for a,b in indices:
            for i in range(n):
                A[i][b]+=1
            for i in range(m):
                A[a][i]+=1
        # print(A)
        return sum(x&1==1 for r in A  for x in r)
" t: M * N + L ; s: M + N"
# https://leetcode.com/problems/cells-with-odd-values-in-a-matrix/submissions/
class Solution:
    def oddCells(self, n: int, m: int, indices: List[List[int]]) -> int:
        col=[False]*m
        row=[False]*n
        for a,b in indices:
            row[a]^=True
            col[b]^=True
        return sum(r^c for r in row for c in col)
"Time: O(L + m + n), space: O(m + n), where L = indices.length"
# https://leetcode.com/problems/cells-with-odd-values-in-a-matrix/submissions/
class Solution:
    def oddCells(self, n: int, m: int, indices: List[List[int]]) -> int:
        odd_rows, odd_cols = [False] * n, [False] * m
        for r, c in indices:
            odd_rows[r] ^= True
            odd_cols[c] ^= True
        # return m * sum(odd_rows) + n * sum(odd_cols) - 2 * sum(odd_rows) * sum(odd_cols)
        return (m - sum(odd_cols)) * sum(odd_rows) + (n - sum(odd_rows))* sum(odd_cols)
"Time: O(L + m + n), space: O(m + n), where L = indices.length"
# https://leetcode.com/problems/cells-with-odd-values-in-a-matrix/submissions/
class Solution:
    def oddCells(self, n: int, m: int, indices: List[List[int]]) -> int:
        odd_rows, odd_cols, cntRow, cntCol = [False] * n, [False] * m, 0, 0
        for r, c in indices:
            odd_rows[r] ^= True
            odd_cols[c] ^= True
            cntRow += 1 if odd_rows[r] else -1 
            cntCol += 1 if odd_cols[c] else -1 
        # return m * cntRow + n * cntCol - 2 * cntRow * cntCol
        return (m - cntCol) * cntRow + (n - cntRow) * cntCol

