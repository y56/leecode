class Solution_TLE:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        ans=[]
        M = len(nums)
        N  = 0
        for r in nums:
            N=max(N,len(r))
        return 
        if M>=N:
            for n in range(0,N):
                rrr = [(n-i,i) for i in range(n+1)]
                for i,j in rrr: # sum as n
                    try:
                        ans.append(nums[i][j])
                    except:
                        break
            tmp = [(N-1-i,i) for i in range(N-1+1)]
            for s in range(1,M-N+1):
                for i,j in tmp:
                    try:
                        ans.append(nums[i+s][j])
                    except:
                        pass
            for n in range(N-2,-1,-1):
                for i,j in [(i,n-i) for i in range(n+1)]: # sum as n
                    try :
                        ans.append(nums[M-1-i][N-1-j])
                    except:
                        pass
        else:
            for n in range(0,M):
                rrr = [(n-i,i) for i in range(n+1)]
                for i,j in rrr: # sum as n
                    try:
                        ans.append(nums[i][j])
                    except:
                        pass
            tmp = [(M-1-i,i) for i in range(M-1+1)]
            for s in range(1,N-M+1):
                for i,j in tmp:
                    try:
                        ans.append(nums[i][j+s])
                    except:
                        pass
            for n in range(M-2,-1,-1):
                for i,j in [(i,n-i) for i in range(n+1)]: # sum as n
                    try :
                        ans.append(nums[M-1-i][N-1-j])
                    except:
                        pass
        return ans

class Solution: # time: O( n*lg(n) ) # space: Theta(n) # n is num of ele
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        diagonals={} 
# a dict to collect ele into a same bucket if they are in same diagonals
        for i,r in enumerate(nums):
            for j,e in enumerate(r):
                if (i+j) in diagonals:
                    diagonals[i+j].append(e)
                else:
                    diagonals[i+j]=[e]
        ans=[]
        
#         Name num of ele as n
#        
#         if the rectangle is full, #diagonals is propotional to sqrt(n)
#         if the rectangle is sparse, #diagonals is propotional to n
#        
#         if we sort keys, time will be diagonals * lg(diagonals)
        
        for i in sorted(diagonals.keys()):
            ans.extend(diagonals[i][::-1])
        return ans
    
class Solution: # time: O(n) # space: Theta(n) # n is num of ele
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        diagonals={} 
# a dict to collect ele into a same bucket if they are in same diagonals
        M=0
        for i,r in enumerate(nums):
            for j,e in enumerate(r):
                M=max(M,i+j)
                if (i+j) in diagonals:
                    diagonals[i+j].append(e)
                else:
                    diagonals[i+j]=[e]
        ans=[]
        for i in range(M+1):
            if i in diagonals:
                ans.extend(diagonals[i][::-1])
        return ans
    
class Solution: # time: Theta(n) # space: Theta min(len(nums),max(len(nums[i]))), which largest len(q) during the algo 
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        ans=[]
        q=[] # q only stores ref
        def helper(ans,q):
            to_remove=[]
            for i,r in enumerate(q):
                # add to ans # remove from row
                ans.append(r.pop(0)) # will be slow bc r is a list, .pop(0) takes too much time
                # deque will be faster but will take extra space
                
                if not r: # if r==[]:
                    to_remove.append(r)  # remember ref # will be remove later
                    # CAUTION! cannot remove on the fly
            for r in to_remove:
                q.remove(r)  # this need linear search in q # len(q) is O(min(len(nums),len(nums[0])))
                # q.remove(r) will run Theta(len(nums))
                
        for r in nums:
            q.insert(0,r) # can use deque # I tried but no diff in time
            helper(ans,q)
        
        # for the rest stuff still in  q
        while q:
            helper(ans,q)
        
        return ans
