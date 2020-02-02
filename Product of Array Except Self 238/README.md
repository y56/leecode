# 238. Product of Array Except Self

Note: Please solve it without division and in O(n).

Follow up:
Could you solve it with constant space complexity? (The output array does not count as extra space for the purpose of space complexity analysis.)

## me
```python=
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left_product = [1] 
        # this `1` is here bc `1` is the Identity Element of Multiplication
        
        for ele in nums[:-1]: # don't want the last
            left_product.append(left_product[-1] * ele)
        
        # left_product[i] is the product of nums[0 ~ i-1]
        
        ans = left_product # copy by ref
        
        right_product = 1
        
        for i, ele in enumerate(nums[-1:0:-1]):
            right_product *= ele
            ans[-2-i] = left_product[-2-i] * right_product
            
        return ans
```
