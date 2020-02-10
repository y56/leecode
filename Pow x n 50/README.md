# 50. Pow(x, n)
```python=
class Solution:
    def myPow(self, x: float, n: int) -> float:
        res = 1.0
        if n < 0:
            x = 1 / x
            n = -n
        while n > 0:
            if (n & 1) == 1:
                res *= x
            x = x ** 2
            n >>= 1
        return res
```
