# 14. Longest Common Prefix
## me,  **Horizontal Scanning**
By the fact that
$$
LCP(S1,​…,Sn​)=LCP(LCP(LCP(S1​,S2​),S3​),…Sn​)
$$
```python=
def longestCommonPrefix(self, strs: List[str]) -> str:

    if not strs: return ''

    def take_common_pre(common_pre, str_):
        index_upper_b = min(len(common_pre), len(str_))
        i = 0
        collect = []
        while i < index_upper_b and common_pre[i] == str_[i]:
            collect.append(common_pre[i])
            i += 1

        return ''.join(collect)

    common_pre = strs[0]
    for str_ in strs[1:]:
        common_pre = take_common_pre(common_pre, str_)
        if common_pre == '':
            return ''
    return common_pre
```

## vertical scanning, me
```python=
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
            if not strs:
                return ''
            str_0 = strs[0]
            for i, c in enumerate(str_0):
                for other in strs[1:]:
                    if i == len(other) or other[i] != c:
                    # ensure index in range
                        return str_0[:i]
            return str_0
```
## vertical scanning, from others
smart! `shortest = min(strs,key=len)`
```python=
def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ''
        shortest = min(strs,key=len) # time: O(# all char)
        for i, ch in enumerate(shortest):
            # all other should be the same with me(the shortest)
            for other in strs:
                if other[i] != ch:
                    # otherwise, we can't go further
                    return shortest[:i]
        return shortest
```

## os.path.commonprefix(strs)

```python=
import os

class Solution:
    # @param {string[]} strs
    # @return {string}
    def longestCommonPrefix(self, strs):
        return os.path.commonprefix(strs)
```

## GOOD! min() max() by alphebetic order 
smart, O(# of all strings)
```python=
class Solution:
    def longestCommonPrefix(self, strs):
        if not strs: return ''

# since list of string will be 
# sorted and retrieved min max by alphebetic order
        s1 = min(strs)
        s2 = max(strs)

        for i, c in enumerate(s1):
            if c != s2[i]:
                return s1[:i] 
                #stop until hit the split index
        return s1

```
## zip(), unpack opera `*`, len(set()) to count # kinds

unpack opera `*`  

### from others
https://realpython.com/python-kwargs-and-args/#unpacking-with-the-asterisk-operators
```python=
class Solution(object):
    def longestCommonPrefix(self, strs):

        sz, ret = zip(*strs), ""
        
        for c in sz:
            if len(set(c)) > 1: break
            ret += c[0]
        return ret
```
```python=
class Solution:
    def longestCommonPrefix(self, strs):
        if not strs:
            return ""
            
        for i, letter_group in enumerate(zip(*strs)):
            if len(set(letter_group)) > 1:
                return strs[0][:i]
        return min(strs)
        # use min(strs) is too much
        # follow the context here, 
        # return min(strs, key=len) is enough
```
```python=
class Solution:
    # @return a string
    def longestCommonPrefix(self, strs):
        if not strs:
            return ""
            
        for i, letter_group in enumerate(zip(*strs)):
            print(i, letter_group)
            if len(set(letter_group)) > 1:
                return strs[0][:i]
        
        # return min(strs)
        return min(strs, key=len)
```
