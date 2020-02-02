# 3. Longest Substring Without Repeating Characters
## me
```python=
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        r = 0
        sofarmaxlen = 0
        set_ = set()
        while r < len(s):
            if s[r] not in set_:
                set_.add(s[r])
                r += 1
                curlen = r - l
                if curlen > sofarmaxlen:
                    sofarmaxlen = curlen
            else:
                set_.remove(s[l])
                l += 1
                
        return sofarmaxlen
```
