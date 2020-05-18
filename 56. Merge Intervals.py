"""
14 min, d(> <)b
"""
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return intervals
        def f(a,b,c,d):
            if a<=c<=b:
                return a,max(b,d)
            return c,d
        ans=[]
        intervals.sort(key=lambda x:x[0])
        l,r=intervals[0]
        intervals.append([float('inf'),None])
        for ll,rr in intervals:
            lll,rrr=f(l,r,ll,rr)
            if lll!=l: # no merge
                ans.append([l,r])
            l,r=lll,rrr  
        return ans
"""
official soln
"""
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x:x[0])
        ans=[]
        for e in intervals:
            if not ans or ans[-1][1]<e[0]: # the right-end of the last ans has no overlap w/ the l
                ans.append(e)
            else: # need to merge
                ans[-1][1]=max(ans[-1][1],e[1])
        return ans
                
                
        
