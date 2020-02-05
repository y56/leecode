# 3. Longest Substring Without Repeating Characters
## me, set(), one-by-one
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
                sofarmaxlen = max(sofarmaxlen, curlen)
            else:
                set_.remove(s[l])
                l += 1
                
        return sofarmaxlen
```
## use dict() to jump
```python=
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        l = 0
        r = 0
        sofarmaxlen = 0
        dict_ = {}
        while r < len(s):
            if s[r]  in dict_:
                l = max(l, dict_[s[r]] + 1) 
# jump to the next of the previously repeating char, 
# if that char is after the starting char we are using right now
            dict_[s[r]] = r 
            curlen = r - l + 1 
# if starting from index 0 and we are now at index 0, 
# the curlen should be 1
            sofarmaxlen = max(sofarmaxlen, curlen)
            r += 1
                                       
        return sofarmaxlen
```
