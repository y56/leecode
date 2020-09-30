class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        
        if 1 not in nums:  # if so, then 1 is the smallest missing positive integer
            return 1
        
        # convert any numbers <=0 into 1
        # also convert any numbers > len(nums)+1 into 1
        # for a list nums w/ len as len(nums), its largest possible "smallest missing positive integer" is len(nums)+1
        # everything remains good if we convert numbers > len(nums)+1 into 1
        for i,x in enumerate(nums):
            if x<=0 or x>len(nums)+1: 
                nums[i]=1
        
        for x in nums:
            # we want to check presence of: 2 ~ len(nums)+1
            # the indices we have: 0 ~ len(nums)-1
            # so we substract by 2
            nums[abs(x)-2]=-abs(nums[abs(x)-2])
            
        for i,x in enumerate(nums):
            if x>0:
                break
        return i+2
            
