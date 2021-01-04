class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        ans=[]
        path=[]
        N=len(candidates)
        candidates.sort(reverse=True) # group same num by sorting # try on large numbers first to fail early
        def backtrack(since,remain):
            if remain==0:
                ans.append(path[:])
            for i in range(since,N):
                if remain-candidates[i]>=0 \
                    and (i==since or # must take this one 
                         candidates[i]!=candidates[i-1]): # to reduce duplicates # only take distinct num after `since`
                    path.append(candidates[i])
                    backtrack(i+1,remain-candidates[i]) # turn into a sub-problem
                    path.pop()
            
        backtrack(0,target)
        return ans
    
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        ans=[]
        path=[]
        counter=Counter(candidates)
        distinct_candidates=list(counter.keys())
        def backtrack(since,remain):
            if remain==0:
                ans.append(path[:])
            for i in range(since,len(distinct_candidates)):
                x=distinct_candidates[i]
                if remain-x>=0 and counter[x]>0:
                    counter[x]-=1
                    path.append(x)
                    backtrack(i,remain-x) # use i not i+1
                    path.pop()
                    counter[x]+=1
        backtrack(0,target)
        return ans
