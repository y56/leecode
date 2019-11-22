# 1100. Find K-Length Substrings With No Repeated Characters

**Python dictionary `dict={}` is much faster than `table=[0]*26`, QQ.**

**Don't use `table=[0]*26` anymore.**


## my try - 00 -  O(N**2)
```python=
class Solution:
    def numKLenSubstrNoRepeats(self, S: str, K: int) -> int:
        n  = len(S)
        ans = 0
        for i in range(n):  # we have n choices to choose a starting point
            countTable = [0] * 26  # initial an countTable
            distinctChar = 0  # initial a counter 
                              # to count how many distinct chars have showed up 
                              # w.r.t. this starting point
            for j in range(i, n):  # Let each starting point to grow
                if countTable[ord(S[j]) - 97] == 0: # 97 = ord('a')
                    distinctChar += 1 # this char shows the 1st time
                    if distinctChar == K: # meet the requirement
                        ans += 1
                else:
                    break  # the string is having duplicated char
                    
                countTable[ord(S[j]) - 97] += 1  # do the count
                
                if distinctChar > K:
                    break  # don't waste time here
        return ans
```
### sideproduct
, which is wrong.
I thought I have to take care substrings with the same look, but I don't have to.
```python=
class Solution:
    def numKLenSubstrNoRepeats(self, S: str, K: int) -> int:
        n  = len(S)
        mySet = set()
        for i in range(n):  # we have n choices to choose a starting point
            countTable = [0] * 26  # initial an countTable
            distinctChar = 0  # initial a counter to count how many distinct chars have showed up w.r.t. this starting point
            for j in range(i, n):  # Let each starting point to grow
                if countTable[ord(S[j]) - 97] == 0: # 97 = ord('a')
                    distinctChar += 1 # this char shows the 1st time
                    if distinctChar == K: # meet the requirement
                        mySet.add(S[i:j+1])
                else:
                    break  # the string is having duplicated char
                    
                countTable[ord(S[j]) - 97] += 1  # do the count
                
                if distinctChar > K:
                    break  # don't waste time here
        print(mySet)
        return len(mySet)
```
## A magic, using a sliding window
rer = 
https://leetcode.com/problems/find-k-length-substrings-with-no-repeated-characters/discuss/333657/Python-O(N)-clever-solution
```python=
class Solution:
    def numKLenSubstrNoRepeats(self, S: str, K: int) -> int:
        l, count = 0, 0
        d = [0] * 26
        for r in range(len(S)):
            d[ord(S[r]) - 97] += 1
            while d[ord(S[r]) - 97] > 1:
                d[ord(S[l]) - 97] -= 1
                l += 1
                print(S[l : r+1])
            if r - l + 1 == K:
                d[ord(S[l]) - 97] -= 1
                print(S[l : r+1])
                l += 1
                count += 1
                print("＝＝＝count")

        return count
```