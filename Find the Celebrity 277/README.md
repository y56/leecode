# 277. Find the Celebrity
## go through columns then the row
```python=
# The knows API is already defined for you.
# return a bool, whether a knows b
# def knows(a: int, b: int) -> bool:

class Solution:
    def findCelebrity(self, n: int) -> int:
        # column_i is all 1s
        # row_i is all 0s except [i][i]
        for be_known in range(n):
            for to_know in range(n):
                if not knows(to_know, be_known):
                    break # try next be_known
            else: # everyone knows him
                celebrity_candidate = be_known
                # let's check if he knows others
                for other in range(n):
                    if knows(celebrity_candidate, other) and celebrity_candidate != other:
                        break
                else:
                    return celebrity_candidate
        return -1
```
## go through columns, exclude some columns, then the row
```python=
def findCelebrity(self, n: int) -> int:
    # want i such that
    # column_i is all 1s
    # row_i is all 0s except [i][i]
    know_others = set() 

    for be_known in range(n):

        if be_known in know_others:
        # this be_known knows someone else, cant't be celebrity
            continue

        for to_know in range(n):

            if knows(to_know, be_known):
            # this to_know knows others, can't be celebrity
                know_others.add(to_know)
                # this be_known is still promising

            else:
                # thers is someone not knowing this be_known
                # this be_known can't be celebrity
                break # try next be_known

        else: # everyone knows him
            celebrity_candidate = be_known
            # let's check if he knows others
            for other in range(n):
                if knows(celebrity_candidate, other) and other != celebrity_candidate:
                    break
            else:
                return celebrity_candidate
    return -1      
```
## t: O(n)
Let's say the final candidate is k.  
It means those before k cannot be the celebrity,  
because they know a previous or current candidate.   
Also, since k knows no one after,   
Those after can't be celebrity either.   
Therefore, k is the only possible celebrity, if there   exists one.  
 
 
- If matrix[i][j] is 1: 
    - row-i cant be celeb  
- If matrix[i][j] is 0: 
    - column-j cant be celeb

```python=
def findCelebrity(self, n: int) -> int:
    # want i such that
    # column_i is all 1s
    # row_i is all 0s except [i][i]

    candidate = 0

    for i in range(1,n):
        if knows(candidate, i): 
        # candi knows `i`, candi can't be celeb
            candidate = i
            # matrix[candidate][i] will always in upper triangle
        else:
        # cand doesn't know `i`, `i` can't be celeb
            pass

    # Everyone should know celeb, and
    # celeb knows none of them except himself.
    for other in range(n):
        if (not knows(other, candidate) or knows(candidate, other)
           ) and other != candidate:
            return -1

    return candidate
```
## **[ BEST ]** guaranteed that `k` doesn't knows those after, so don't check that
```python=
def findCelebrity(self, n: int) -> int:

    candidate = 0

    for i in range(1,n):
        if knows(candidate, i): 
        # candi knows `i`, candi can't be celeb
            candidate = i
            # matrix[candidate][i] will always in upper triangle
        else:
        # cand doesn't know `i`, `i` can't be celeb
            pass

    # For everyone should know celeb
    for other in range(n):
        if not knows(other, candidate):
            return -1

    # celeb knows none of others.
    # BUT, for those larger than candidate,
    # we already knew that candidate knows none of them,
    # only have to chek if candidate smaller ones.
    for other_smaller in range(candidate):
        if knows(candidate, other_smaller):
            return -1
    # 整個豎的 都要是1
    # matrix[cand][cand]以左 都要是0

    return candidate
```
## 
https://leetcode.com/problems/find-the-celebrity/discuss/434538/JAVA-O(N)-greater-illustrations-to-show-why-it-works

![image alt](https://assets.leetcode.com/users/soccer_player/image_1574358361.png)
## 
![](https://i.imgur.com/GshArEw.jpg)


## Is it guaranteed that all elements above [k][k] are 1s?
