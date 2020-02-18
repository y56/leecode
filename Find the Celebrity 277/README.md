# 277. Find the Celebrity
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
