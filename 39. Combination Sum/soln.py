class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort(reverse=True) # large candicates to be tried first; this will let the algo fail earlier 
        ans=[]
        def helper(path,target,start):
            if target==0:
                ans.append(path[:])
            for i in range(start,len(candidates)): # we can only use those in candidates[start:]
                x=candidates[i]
                if x<=target: # go deeper only when hopeful; stop recursion earlier save much time
                    helper(path+[x], target-x, i) # use i as `start` for next recursion
        helper([],target,0)
        return ans
"""
roughly same time by these two soln
"""
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort(reverse=True) # large candicates to be tried first; this will let the algo fail earlier 
        ans=[]
        path=[]
        def helper(target,start):
            if target==0:
                ans.append(path[:])
            # elif target>0:
            for i in range(start,len(candidates)): # we can only use those in candidates[start:]
                x=candidates[i]
                if x<=target: # go deeper only when hopeful; stop recursion earlier save much time
                    path.append(x)
                    helper(target-x, i) # use i as `start` for next recursion
                    path.pop()
        helper(target,0)
        return ans
