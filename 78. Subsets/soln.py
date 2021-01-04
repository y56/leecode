class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans=[[]]
        for x in nums:
            new_ans=[]
            for pre in ans:
                new_ans.append(pre[:])
                new_ans.append(pre+[x])
            ans=new_ans
        return ans
    
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans=[[]]
        for x in nums:
            tmp=[]
            for pre in ans:
                tmp.append(pre+[x])
            ans+=tmp
        return ans
    
"""
fastest
"""
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans=[[]]
        for x in nums:
            ans+=[pre+[x] for pre in ans]
        return ans
    
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        path=[]
        ans=[]
        def dfs(cur):
            ans.append(path[:])
            for i in range(cur,len(nums)):
                path.append(nums[i])
                dfs(i+1)
                path.pop()
        dfs(0)
        return ans    
    
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        N=len(nums)
        ans=[]
        for bits in range(2<<N-1):
            tmp=[]
            for b_pos in range(N):
                if bits&1==1:
                    tmp.append(nums[b_pos])
                bits>>=1
            ans.append(tmp)
        return ans    
            

