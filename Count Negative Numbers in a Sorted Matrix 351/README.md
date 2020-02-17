# 351. Count Negative Numbers in a Sorted Matrix
## O(m+n)
```python=
class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        ans = 0
        right_bound = row_len = len(grid[0])
        for row in grid:
            i = 0
            while i < right_bound and row[i] >= 0:
                i += 1
            ans += row_len - i
            right_bound = i
        return ans
```
## O(m*n)
```python=
class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        ans = 0
        for row in grid:
            for ele in row:
                if ele < 0:
                    ans += 1
        return ans
```
