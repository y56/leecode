"""
dfs/backtrack w/ swap
"""
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n=len(nums)
        ans=[]
        def helper(i):
            if i==n:
                ans.append(nums[:])
            for j in range(i,n):
                nums[i],nums[j]=nums[j],nums[i]
                helper(i+1)
                nums[i],nums[j]=nums[j],nums[i]
        helper(0)
        return ans
"""
dfs w/ all needed info passed down
"""
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n=len(nums)
        ans=[]
        def dfs(path,can_use):
            if not can_use:
                ans.append(path)
            for i,x in enumerate(can_use):
                dfs(path+[x],can_use[:i]+can_use[i+1:])
        dfs([],nums)
        return ans
"""
dfs/backtrack with append(), pop() and public counter 
"""
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n=len(nums)
        counter={x:1 for x in nums}
        ans=[]
        def backtrack(path):
            if len(path)==len(nums): # reach desired len
                ans.append(path[:])
            for x in nums:
                if counter[x]==1:
                    path.append(x)
                    counter[x]-=1
                    backtrack(path)
                    path.pop()
                    counter[x]+=1
        backtrack([])
        return ans
"""
intuitive recursion
"""
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if not nums:
                return [[]]
        ans=[]
        for i,num in enumerate(nums):
            for permutation_of_the_rest in self.permute(nums[:i]+nums[i+1:]):
                ans.append([num]+permutation_of_the_rest)
        return ans
