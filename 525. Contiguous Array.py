class TLE_Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        if nums==[]:
            return 0
        
        acc=[0] # accumulation
        for ele in nums:
            acc.append(acc[-1]+ele)
        # print(acc)
        q=[ ( 1-len(nums)-1, 
              1, 
              len(nums)) ]
        #  minus length, start pt, end pt
        ans=0
        while q:
            # print(q)
            L,i,j=heapq.heappop(q)
            L=-L
            n1=acc[j]-acc[i-1]
            n0=L-n1
            diff=abs(n1-n0)
            if ans>=L:
                continue
            if diff==L:
                continue
            if diff==0:
                ans=max(ans,L)
            for k in range(0,diff+1):
                heapq.heappush(q, (-L+diff,i+diff-k,j-k))
        return ans
class TLE_Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        if nums==[]:
            return 0
        
        acc=[0] # accumulation
        for ele in nums:
            acc.append(acc[-1]+ele)
        # print(acc)
        q=collections.deque([ ( 1, 
                                len(nums)) ])
        #  minus length, start pt, end pt
        ans=0
        while q:
            # print(q)
            i,j=q.popleft()
            n1=acc[j]-acc[i-1]
            L=j-i+1
            n0=L-n1
            diff=abs(n1-n0)
            if ans>=L:
                continue
            if diff==L:
                continue
            if diff==0:
                ans=max(ans,L)
                continue
            for k in range(0,diff+1):
                q.append(  (i+diff-k,
                            j-k)  )
        return ans    
class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        ct=0
        d={0:0}
        ans=0
        for i,ele in enumerate(nums):
            if ele==1:
                ct+=1
            else: # ele==0:
                ct-=1
            if ct not in d:
                d[ct]=i+1
            else:
                ans=max(ans,i - d[ct] + 1)
        return ans
class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        ct=0
        N=len(nums)
        # possible value of ct is: -N~0~N
        d=[-1]*(2*N+1) # hand-made hash-talbe
        d[N+0]=0
        ans=0
        for i,ele in enumerate(nums):
            if ele==1:
                ct+=1
            else: # ele==0:
                ct-=1
            if d[N+ct]==-1: # yet visited
                d[N+ct]=i+1 # remember the first index when we see this ct
            else:
                ans=max(ans,i - d[N+ct] + 1)
        return ans
