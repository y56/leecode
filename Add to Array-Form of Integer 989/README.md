# 989. Add to Array-Form of Integer
```python=
class Solution:
    def addToArrayForm(self, A: List[int], K: int) -> List[int]:
        
        def add1dig(A, dig, pos):
            if pos == len(A): 
# the list is going to have one more digit on the left-most position
                A.insert(0, dig)
                return
            tmp = A[~pos] + dig
            A[~pos] = tmp % 10
            if tmp < 10:
                return
            add1dig(A, tmp // 10, pos + 1)
        
        pos = 0 
# position is defined as the last element of the list is 0
        while K > 0:
            dig = K % 10
            add1dig(A, dig, pos)
            pos += 1
            K //= 10
        return A
```
