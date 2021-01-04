"""
faster
"""
class Solution:
    def countArrangement(self, N: int) -> int:
        li=list(range(0,N+1)) # 1-indexing #  0 is useless
        self.ans=0
        def backtrack(right): # swap from RHS
# from RHS is better since larger numbers are less likely to be Beautiful
# if we start from left to right there will be too many false hopes
            if right==0: # reach the left bound
                self.ans+=1
            for left in range(right,0,-1): 
                li[left],li[right]=li[right],li[left]
                if li[right] % right == 0 or right % li[right] == 0: 
                # if Beautiful for this pos `right` then go deeper
                    backtrack(right-1)
                li[left],li[right]=li[right],li[left]
        backtrack(N)
        return self.ans
"""
slower
"""
class Solution:
    def countArrangement(self, N: int) -> int:
        
        def beautiful(num,pos):
            return num % pos == 0 or pos % num == 0
        
        nums=list(range(N,0,-1)) # n ~ 1
        counter=[1]*(N+1) # 0th is useless
        self.ans=0
        
        def backtrack(pos): 
            if pos == 0: # means all pos are filled
                self.ans+=1
                
            for num in nums: # try on all nums # all numbers N~1 # try on large num first
                if counter[num]>0 and beautiful(num,pos): 
# if still not used up then we can use it # check if beautiful
                    counter[num]-=1
                    backtrack(pos-1) # go fill the next one
                    counter[num]+=1
                
        backtrack(N) # start from the last pos
        return self.ans
