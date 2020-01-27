# 69. Sqrt(x)
## 
```python=
class Solution:
    def mySqrt(self, x):
        if x == 0: return 0
        if x < 4: return 1
        l = 2
        r = x // 2 + 1
        while r > l:
            m = (l + r) // 2
            m2 = m ** 2
            if m2 > x:
                r = m
            elif m2 < x:
                l = m
            else: # ==
                return m
            if r == l+1: 
                return l
```
