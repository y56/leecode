# 283. Move Zeroes
```python
"""
Do not return anything, modify nums in-place instead.
"""
```
## while, if, del, list-concatenation
```python=
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        count = 0
        i = 0
        while i < len(nums): 
        # Note that len(nums) is changing.
            if nums[i] == 0:
                del nums[i]
                count += 1
                i -= 1
            i += 1
        
        nums += [0] * count
```
## array-like swap
```python=
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        i = 0
        end_of_checking_region = len(nums) - 1 
        while i <= end_of_checking_region:
            if nums[i] == 0:
                j = i # j is for swaping
                while j + 1 <= end_of_checking_region:
                    nums[j] = nums[j + 1]
                    j += 1
                nums[end_of_checking_region] = 0
                end_of_checking_region -= 1
                i -= 1  # I forgot to add this line
            i += 1
```
## another list, careful of pass-by-address
### correct
```python=
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        print(id(nums))        
        ans = []
        for ele in nums:
            if ele != 0:
                ans.append(ele)
        nums[:] = ans + [0] * (len(nums) - len(ans))
        # modifying the content through dereferencing
        print(id(ans))
        print(ans)
        print(id(nums))
        print(nums)
```
```python
140634032574144
140634032546688
[1, 3, 12]
140634032574144
[1, 3, 12, 0, 0]
```
### wrong
```python=
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        print(id(nums))        
        ans = []
        for ele in nums:
            if ele != 0:
                ans.append(ele)
        nums = ans + [0] * (len(nums) - len(ans))
        # re-assign without dereferencing
        # merely replace it's content with a new address
        print(id(ans))
        print(ans)
        print(id(nums))
        print(nums)
```
```python
140117590762368
140117577713088
[1, 3, 12]
140117580755520
[1, 3, 12, 0, 0]
```
### wrong
```python=
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        print(id(nums))        
        ans = []
        print(id(ans))
        for ele in nums:
            if ele != 0:
                ans.append(ele)
        ans = ans + [0] * (len(nums) - len(ans))
        nums = ans
        print(id(ans))
        print(ans)
        print(id(nums))
        print(nums)
```
```python
139993888059136
139993888331264
139993891373760
[1, 3, 12, 0, 0]
139993891373760
[1, 3, 12, 0, 0]
```
### correct
```python=
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        print(id(nums))        
        ans = []
        print(id(ans))
        for ele in nums:
            if ele != 0:
                ans.append(ele)
        ans = ans + [0] * (len(nums) - len(ans))
        nums[:] = ans
        print(id(ans))
        print(ans)
        print(id(nums))
        print(nums)
```
```python
140323033681280
140323033653824
140323036705280
[1, 3, 12, 0, 0]
140323033681280
[1, 3, 12, 0, 0]
```
## for, no if, concatenation
```python=
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        non_zero_count = 0
        for ele in nums:
            nums[non_zero_count] = ele
            # copying a zero to overwrite a zero will happen
            # but it's fine
            non_zero_count += (ele != 0)
        
        nums[non_zero_count::] = [0] * (len(nums) - non_zero_count)

```
## for, swap
### wrong
```python=
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        non_zero_count = 0
        for ele in nums:
            if ele != 0:
                nums[non_zero_count], ele = ele, nums[non_zero_count]
                non_zero_count += 1
```
### correct
```python=
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        non_zero_count = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[non_zero_count], nums[i] = nums[i], nums[non_zero_count]
                non_zero_count += 1
```
## sort, key
```python=
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        nums.sort(key=lambda x: 0 if x else 1)
```
## count, remove, append
```python=
class Solution:
    def moveZeroes(self, nums):
        for i in range(0,nums.count(0)):
            nums.remove(0)
            nums.append(0)
```
## count(), one-line-for
```python=
class Solution:
    def moveZeroes(self, nums):
        if len(nums) > 0:
            count = nums.count(0)
            nums[:] = [value for value in nums if value != 0]
            nums.extend([0] * count)
```
## nums.sort(key=bool, reverse=True) 
```python=
class Solution:
    def moveZeroes(self, nums):
        nums.sort(key=bool, reverse=True)
```
## del, append, while
```python=
class Solution(object):
    def moveZeroes(self, nums):
        i = 0
        end = len(nums)
        while i < end:
            if nums[i] == 0:
                del nums[i]
                nums.append(0)
                end -= 1
            else:
                i += 1
```