# 415. Add Strings
## 
```python=
class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        def add1dig(li, dig: str, pos):
            if pos == len(li):
                li.insert(0, dig)
                return 
            tmp = int(li[~pos]) + int(dig)
            li[~pos] = str(tmp % 10)
            if tmp < 10:
                return 
            add1dig(li, str(tmp // 10), pos + 1)
        
        pos = 0
        li = list(num1) # str to list
        while pos < len(num2): # 
            d = num2[~pos]
            add1dig(li, d, pos)
            pos += 1
        return ''.join(li)
```
## 
```python=
class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        def add1dig(li, dig: str, pos):
            if pos == len(li):
                li.append(dig)
                return 
            tmp = int(li[pos]) + int(dig)
            li[pos] = str(tmp % 10)
            if tmp < 10:
                return 
            add1dig(li, str(tmp // 10), pos + 1)
        
        pos = 0
        li = list(num1)[::-1] # so we can use append(), faster than insert() at head
        len_num2 = len(num2)
        while pos < len_num2:
            d = num2[~pos]
            add1dig(li, d, pos)
            pos += 1
        return ''.join(li[::-1])
        
```
