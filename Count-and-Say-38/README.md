# 38. Count and Say
## 
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
                # storge the before
                    res.extend(str(count), char)
                # be ready to count a new char
                    char = ele
                    count = 1
            res.extend(str(count), char)
            
            return res
        
        s = '1'
        
        for _ in range(n-1):
            s = helper(s)
            
        return s
```
