# 66. Plus One
## 
```python=
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        for i, digit in enumerate(digits[::-1]):
            if digit + 1 < 10:
                digits[~i] = digit + 1
                break
            else:
                digits[~i] = (digit + 1) % 10
        else:
            digits.insert(0, 1)
        return digits
```
