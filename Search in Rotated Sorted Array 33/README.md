# 33. Search in Rotated Sorted Array
## find index of the smallest, then usual binary search
```python=
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        def find_index_min(nums):
            if nums[0] <= nums[-1]:  
            # use <= instead < to catch nums as [5]
                return 0
            l = 0 
            r = len(nums) - 1
            while r >= l:
                pivot = (l + r) // 2
                if nums[pivot] > nums[pivot + 1]:
                    return  pivot + 1
                else:
                    if nums[pivot] < nums[-1]:
                        r  = pivot - 1
                    else:
                        l = pivot + 1
            
        def rotated_index(normal_index):
            if normal_index + index_min >= len(nums):
                return normal_index + index_min - len(nums)
            return normal_index + index_min
        
        # we need this
        if not nums:
            return -1
        
        index_min = find_index_min(nums)
        
        l = 0
        r = len(nums) - 1

        while r >= l:
            pivot = (l + r) // 2
            if nums[rotated_index(pivot)] == target:
                return rotated_index(pivot)
            else:
                if nums[rotated_index(pivot)]  < target:
                    l  = pivot + 1
                else:
                    r = pivot - 1
        return -1

```
## one pass
```python=
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0 
        r = len(nums) - 1
        while l <= r:
            m = (l + r) // 2 # using floor leads to nums[m] >= nums[l]:
            if nums[m] == target:
                return m
            elif nums[m] >= nums[l]: # m~l is sorted # interrupt at l~r
                if nums[l] <= target < nums[m]:
                    r = m - 1
                else: 
                    l = m + 1
                
            else: # nums[m] < nums[l] # interrupt ar l~m # m~r is sorted
                if nums[m] < target  <= nums[r]:
                    l = m + 1
                else:
                    r = m - 1
        return -1 
```
```python=
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0 
        r = len(nums) - 1
        while l <= r:
            m = (l + r + 1) // 2 # using ceil leads to nums[m] > nums[l]:
            if nums[m] == target:
                return m
            elif nums[m] > nums[l]: # m~l is sorted # interrupt at l~r
                if nums[l] <= target < nums[m]:
                    r = m - 1
                else: 
                    l = m + 1
                
            else: # nums[m] < nums[l] # interrupt ar l~m # m~r is sorted
                if nums[m] < target  <= nums[r]:
                    l = m + 1
                else:
                    r = m - 1
        return -1 
```
