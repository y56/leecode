class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        ans=[]
        def dfs(k,n,i,path): # i is for the current discussed number
            if k==0: # no number for you to use
                if n==0: # remaining is 0, good
                    ans.append(path)
                else:
                    return # terminate the search
                
            # so here k>0
            elif i>0 and n>0: 
                # if i==0, we have gone through 9~1, no more work
                # if the remaining n<0, no more hope, can stop
                # if k>0 and n==0, no more hope, can stop
                dfs(k-1,n-i,i-1,path+[i])
                dfs(k,n,i-1,path+[])
                
        dfs(k,n,9,[])
        return ans

class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        ans=[]
        def dfs(k,n,i,path):
            if k==0 and n==0:
                ans.append(path)
                return 
            if k<=0 or n<=0 or i==0:
                return
            dfs(k-1,n-i,i-1,path+[i])
            dfs(k,n,i-1,path+[])
                
        dfs(k,n,9,[])
        return ans
    
class Solution:
    def combinationSum3(self, k, n):
        return [c for c in combinations(range(1, 10), k) if sum(c) == n]

