"""
https://imgur.com/U93qCOq
"""
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        def backtrack(left):
            if len(li)==k:
                ans.append(li[:])
            for i in range(left,n+1):
                li.append(i)
                backtrack(i+1)
                li.pop()
        ans=[]
        li=[]
        backtrack(1)    
        return ans
                
                
#######################################################################
class Solution: 
    """
    official soln
    """
    def combine(self, n: int, k: int) -> List[List[int]]:
        # init first combination
        nums = list(range(1, k + 1)) + [n + 1]
        
        output, j = [], 0
        while j < k:
            # add current combination
            output.append(nums[:k])
            print(nums[:k])
            # increase first nums[j] by one
            # if nums[j] + 1 != nums[j + 1]
            j = 0
            while j < k and nums[j + 1] == nums[j] + 1:
                nums[j] = j + 1
                j += 1
                print("            reset",nums)
            nums[j] += 1
            print("            add  ",nums)
        return output
class Solution:
    """
    same logic w/ official soln
    """
    def combine(self, n: int, k: int) -> List[List[int]]:
        # init first combination
        nums = list(range(1, k + 1))
        output = []
        while True:
            output.append(nums[:])
            if nums[0]==n-k+1: break # the last combi # n-k+1 ~ n
            for j in range(k):
                if j==k-1: # the last one always do +1 can't do reset
                    nums[j]+=1
                else:
                    if nums[j + 1] == nums[j] + 1: # 
                        nums[j] = j + 1 # reset
                    else:
                        nums[j] += 1
                        break
        return output
class Solution:
    """
    make if/else look better
    """
    def combine(self, n: int, k: int) -> List[List[int]]:
        # init first combination
        nums = list(range(1, k + 1))
        output = []
        while True:
            output.append(nums[:])
            if nums[0]==n-k+1: break # the last combi # n-k+1 ~ n
            for j in range(k):
                if j==k-1 or not nums[j+1]==nums[j]+1: 
                # for the last one always do +1 can't do reset
                # for middle ones, if next > me+1, me+=1
                    nums[j]+=1
                    break # this break is only for middle ones
                else:
                    nums[j] = j + 1 # reset me if next==me+1
        return output
    
# to list all combinations, to list all non-decreasing sequence, and to list all methods to go through a grid, are the samw problem.
"""
https://imgur.com/aoVxJ6r
"""

