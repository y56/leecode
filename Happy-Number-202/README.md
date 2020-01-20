# 202. Happy Number

## hashtable/set()
```python=
class Solution:
    def isHappy(self, n: int) -> bool:
        
        def helper(n):
            sum_ = sum(int(c)**2 for c in str(n))
            return sum_
        
        set_ = set()
        while n not in set_:
            if n == 1:
                return True
            set_.add(n)
            n = helper(n)
        return False  
```
## Floyd cycle detection aka tortoise-hare-race
```python=
class Solution:
    def isHappy(self, n: int) -> bool:
        
        def helper(n):
            sum_ = sum(int(c) ** 2 for c in str(n))
            return sum_
        
        slow = n
        fast = helper(n)
        while slow != fast and fast != 1:
            slow = helper(slow)
            fast = helper(helper(fast))
        if 1 == fast:
            return True
        return False
```