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
