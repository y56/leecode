class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans=[]
        def btrack(s,l,r):
            if len(s)==2*n:
                ans.append(s)
                return 
            if l<n:
                btrack(s+'(',l+1,r)
            if r<l:
                btrack(s+')',l,r+1)
        btrack('',0,0)
        return ans

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        @lru_cache(None)
        def f(n):
            if n==0: return ['']
            res=[]
            for nn in range(n):
                for a in f(nn):
                    for b in f(n-1-nn):
                        res.append('('+a+')'+b)
            return res
        return f(n)

