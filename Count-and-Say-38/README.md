# 38. Count and Say
## me
```python=
class Solution:
    def countAndSay(self, n: int) -> str:
        
        def helper(s):
            
            char = s[0]
            count = 0
            res = ''
            for ele in s:
                if ele == char:
                    count += 1
                else:
                    # store the before
                    res += str(count) + char
                    # be ready to count a new char
                    char = ele
                    count = 1  # !!! already one count
            res += str(count) + char
            
            return res
        
        s = '1'
        
        for _ in range(n-1):
            s = helper(s)
            
        return s
```
## `.join()` is faster than `+=`
https://stackoverflow.com/questions/39312099/why-is-join-faster-than-in-python

Since strings are allocated in memory in array style.

Grow in list, convert to string only once.

```python=
class Solution:
    def countAndSay(self, n: int) -> str:
        
        def helper(s):
            
            char = s[0]
            count = 0
            res = []
            for ele in s:
                if ele == char:
                    count += 1
                else:
                    # store the before
                    res.extend([str(count), char])
                    # be ready to count a new char
                    char = ele
                    count = 1  # !!! already one count
            res.extend([str(count), char])
            
            return ''.join(res)
        
        s = '1'
        
        for _ in range(n-1):
            s = helper(s)
            
        return s
```
## while
```python=
def helper(s):
    
    result = []
    startptr = 0
    while startptr < len(s):
        curptr = startptr + 1
        while curptr < len(s) and s[startptr] == s[curptr]:
            curptr += 1
        result.extend([str(curptr - startptr), s[startptr]])
        startptr = curptr
    return ''.join(result)

class Solution:
    def countAndSay(self, n: int) -> str:
        
        s = '1'
        
        for _ in range(n-1):
            s = helper(s)
            
        return s
```
## itertools.groupby()
really cool
```python=
import itertools
def countAndSay(self, n: int) -> str:
    s = '1'
    for _ in range(n - 1):
        s = ''.join(str(len(list(group))) + digit
                    for digit, group in itertools.groupby(s))
    return s
```