# 75. Sort Colors
## me, two pass
```python=
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count0 = 0
        count1 = 0
        count2 = 0
        for ele in nums: 
            if ele == 0:
                count0 += 1
            if ele == 1:
                count1 += 1
            if ele == 2:
                count2 += 1
        for i in range(count0):
            nums[i] = 0
        for i in range(count0, count0 + count1):
            nums[i] = 1
        for i in range(count0 + count1, count0 + count1 + count2):
            nums[i] = 2
```
## me, two pass
```python=
class Solution:
    def sortColors(self, nums: List[int]) -> None:

        counts = [0, 0, 0]
        for ele in nums: 
            counts[ele] += 1
        i = 0
        for num, count in enumerate(counts):
            nums[i: i + count + 1] = [num] * count
            i += count
```
## one pass
```python=
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        p0r = 0
        p2l = len(nums) - 1
        curr = 0
        
        # while p0r - 1 < curr < p2l + 1: # too much conditions
        while curr < p2l + 1:
            
            if nums[curr] == 0:
            
                nums[p0r], nums[curr] = nums[curr], nums[p0r]
                
                curr += 1
                p0r += 1
                
            elif nums[curr] == 1:
                curr += 1
            else: 
                nums[p2l], nums[curr] = nums[curr], nums[p2l]
                p2l -= 1
```
## 
```python=
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        p0r = 0
        p2l = len(nums) - 1
        curr = 0
        
        while curr < p2l + 1:
        
            if nums[curr] == 0:
            
                nums[p0r], nums[curr] = nums[curr], nums[p0r]
                
                curr += 1
                p0r += 1
                
                continue # this is necessary
                
            if nums[curr] == 1:
            
                curr += 1
                
                continue # this is necessary
                
            if nums[curr] == 2:
            
                nums[p2l], nums[curr] = nums[curr], nums[p2l]
                p2l -= 1
                
                continue # this is necessary
```
