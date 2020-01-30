# 387. First Unique Character in a String
## me
```python=
class Solution:
    def firstUniqChar(self, s: str) -> int:
        if not s: 
            return -1
        set_seem = set()
        set_dup = set()
        for c in s:
            if c in set_seem:
                set_dup.add(c) 
            set_seem.add(c)
            
        for i, c in enumerate(s): 
            if c not in set_dup:
                return i
        
        return -1
```
## count = collections.Counter(s)
```python=
class Solution:
    def firstUniqChar(self, s: str) -> int:
        count = collections.Counter(s)
        for i, c in enumerate(s):
            if count[c] == 1:
                return i
        return -1
```
