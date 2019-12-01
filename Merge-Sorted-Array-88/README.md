###### tags: `leetcode`

# 88. Merge Sorted Array

## Array Style
```python=
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # array style
        # pretend that I am playin w/ a real array
        nums1[n:] = nums1[0:m]  # right-shift content of nums1 w/ n elements 
        # nums1[0+n:m+n] = nums1[0:m]
        i =  i1 = i2 = 0
        while i1 < m and i2 < n:
            if nums1[n+i1] <= nums2[i2]:
                nums1[i] = nums1[n+i1]
                i1 += 1
                i += 1
            else:
                nums1[i] = nums2[i2]
                i2 += 1
                i += 1
        if i1 == m:  # nums1 is used up.
            nums1[i:] = nums2[i2:]
        # For the case where nums2 is used up, we don't have to do anything.
        # Since nums1 is already there, 
        # we don't need to pour the rest of nums1 to the merged nums1.
        # They are already there.
        # So we can ignore the `else` here. 
        # else:
        #     nums1[i:] = nums1[n+i1:]
            
```
## Array Style, Better, Don't Need to Copy, Pick the Larger
```python=
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # array style
        # pretend that I am playin w/ a real array
        i = m + n - 1
        i1 = m - 1
        i2 = n - 1
        while i1 >= 0 and i2 >= 0:
            if nums1[i1] > nums2[i2]:
                nums1[i] = nums1[i1]
                i1 -= 1
                i -= 1
            else:
                nums1[i] = nums2[i2]
                i2 -= 1
                i -= 1
        if i1 < 0:  # nums1 is used up. 
            # Pour the rest nums2 to the front side of nums1 
            nums1[:i+1] = nums2[:i2+1]
        else:
            nums1[:i+1] = nums1[:i1+1]
```
## Python's Linked List Style, Not Accepted But Correct
It seems like that Leetcode is checking the content of that reference, not the content of the variable `nums1`. 
```python=
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # python's linked list style
        nums1_ = nums1[0:m]
        nums1 = []  # It has a new ref now. 
        # All the modification will be on the new ref.
        
        while nums1_ and nums2:
            if nums1_[0] <= nums2[0]:
                nums1.append(nums1_.pop(0))
            else:
                nums1.append(nums2.pop(0))
        if nums1_:  # nums1_ is yet used up.
            nums1 += nums1_
        else:
            nums1 += nums2
        print(nums1)
```
```python=
Wrong Answer

Your input
[1,2,3,0,0,0]
3
[2,5,6]
3
stdout
[1, 2, 2, 3, 5, 6]  # the printout is correct
Output
[1,2,3,0,0,0]  # but the data on that ref remain the same
Expected
[1,2,2,3,5,6]
```
## Python's Linked List Style, Accepted
```python=
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # python's linked list style
        nums1_ = nums1[0:m]
        tmp = []
        while nums1_ and nums2:
            if nums1_[0] <= nums2[0]:
                tmp.append(nums1_.pop(0))
            else:
                tmp.append(nums2.pop(0))
        if nums1_:  # nums1_ is yet used up.
            tmp += nums1_
        else:
            tmp += nums2
        nums1[:] = tmp[:]            
```
## Python's Linked List Style, Accepted, Meaningful
### In Python, **Object references are passed by value**, so it works.
```python=
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # python's linked list style
        nums1_ = nums1[0:m]  # copy by value
        tmp = nums1  # copy ref by value
        nums1 = []  # This var gets a new ref.
        while nums1_ and nums2:
            if nums1_[0] <= nums2[0]:
                nums1.append(nums1_.pop(0))
            else:
                nums1.append(nums2.pop(0))
        if nums1_:  # nums1_ is yet used up.
            nums1 += nums1_
        else:
            nums1 += nums2
        print(nums1)
        tmp[:] = nums1[:]  # copy by value to the desired ref     
```
## Python's Linked List Style, Accepted, Very Meaningful
### `nums1[:] = []` keeps the ref and clean the contents
```python=
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # python's linked list style
        nums1_ = nums1[0:m]
        nums1[:] = []  # !!! critical !!!
        while nums1_ and nums2:
            if nums1_[0] <= nums2[0]:
                nums1.append(nums1_.pop(0))
            else:
                nums1.append(nums2.pop(0))
        if nums1_:  # nums1_ is yet used up.
            nums1 += nums1_
        else:
            nums1 += nums2

```