""" 23 min 30 sec """
class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        if not nums: 
            return 0
        l,r=0,0
        sum_=nums[0] # for now sum_ is 0~0
        ans=len(nums)+1 # or you can use float('inf')
        
        # if sum_ too small, grow it
        while sum_<s and r+1<len(nums):
            r+=1
            sum_+=nums[r]
            
            # if sum_ large enough, shrink it
            if sum_>=s and l<=r:
                while sum_>=s and l<=r:
                    sum_-=nums[l]
                    l+=1
                # only update ans if we can enter inner-loop
                # and only update it once when leaving inner-loop
                ans=min(ans,r-l+1+1)
                
        if ans==len(nums)+1:
            if nums[0]>=s: # this means never entering outer-while
                return 1
            return 0 # this means sum(nums)<s
        return ans
