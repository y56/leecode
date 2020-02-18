# 74. Search a 2D Matrix
```python=
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False
        rowlen = len(matrix[0])
        l = 0
        r = rowlen * len(matrix) - 1
        while l <= r:
            m = (l + r) // 2
            row, col = m // rowlen, m % rowlen
            candidate = matrix[row][col]
            if candidate == target:
                return True
            else:
                if candidate < target:
                    l = m + 1
                else:
                    r = m - 1
        return False
```
