# 15. 3Sum
## from another person
```python=
class Solution(object):
	def threeSum(self, nums):
		res = []
		nums.sort()
		length = len(nums)
		for i in range(length-2): # we are checking i with (i++)~(last--) 
                                  # so no need to check the last two elements
			if nums[i]>0: break # all positive after here, go to return
			if i>0 and nums[i]==nums[i-1]: continue # if it is not the 0th,
                                                    # check if it is the same
                                                    # so that we can skip it

			l, r = i+1, length-1 # two ptr after i, approaching each other
            
			while l < r:
				total = nums[i]+nums[l]+nums[r]

				if total<0: # too small, but the larger can't be larger,
					l+=1    # so let the smaller go larger
				elif total>0: # too large, but the smaller can't be smaller,
					r-=1      # # so let the larger go smaller
				else: # Bingo! Got what we want
					res.append([nums[i], nums[l], nums[r]])
					while l<r and nums[l]==nums[l+1]: # a repeating left,
						l+=1                          # move until different
					while l<r and nums[r]==nums[r-1]: # a repeating right,
						r-=1                          # move until different
					l+=1
					r-=1
		return res
```