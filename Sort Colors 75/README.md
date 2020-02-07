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
