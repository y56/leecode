# 42. Trapping Rain Water
## brute force

```python=
class Solution:
    def trap(self, height: List[int]) -> int:
        ans = 0
        for i, x in enumerate(height):
            Lmax = Rmax = x
            for j, y in enumerate(height[0:i+1]):
                Lmax = max(y, Lmax)
            for k, z in enumerate(height[i::]):
                Rmax = max(z, Rmax)
            ans += min(Lmax, Rmax) - x
            
        return ans
```

## DP
:::danger
I forgot to do 
```
    if not height:
        return 0
```
and `Lmax = height[0]` had  index-out-of-range.
:::
```python=
class Solution:
    def trap(self, height: List[int]) -> int:
        
        if not height:
            return 0
        
        Lmax = height[0]  # initiate
        Lmax_list =[]
        for i, x  in enumerate(height):
            Lmax = max(x, Lmax)
            Lmax_list.append(Lmax)
        
        Rmax = height[-1]  # initiate
        Rmax_list =[]
        for i, x  in enumerate(height[::-1]):
            Rmax = max(x, Rmax)
            Rmax_list.insert(0, Rmax)
        
        ans = 0
        for j, y in enumerate(height):            
            ans += min(Lmax_list[j], Rmax_list[j]) - y

        return ans
```

## THE HOLLY STACK
If a current bar is higher than the bar in the top of the stack, 
we can't push it to the stack.   

We shall fill the hole with water and count the water; and remove those bars shorter than the current bar from the stack.   

Then, we push the current bar to the stack.   

As the result, the bars in the stack are non-strictly decreasing , from base to top.   

### algorithm

![](https://i.imgur.com/iaSDzAR.png)


```python=
def trap(self, height: List[int]) -> int:
    stack = []
    ans = 0  # accumulative sum
    cur_i = 0  # current index

    while cur_i < len(height):  # not out of range

        while stack and height[cur_i] > height[stack[-1]]:  
        # the check for stack in this line is only for the first time
        # we count water only when the bar goes high 

            mytop = stack.pop()  
            # hold the bar in the middle in my hand, but we might not need it

            if not stack:  # There are no left bound for water. 
                break      # We are only popping the stack. No water to count.

            bounded_height = min(  height[cur_i], 
                                 height[stack[-1]]  ) - height[mytop]
            # bounded by the lower bar
            # we count one layer of water here and fill it. 
            # Let the later loops count the other higher water

            horizontal_index_distance = cur_i - stack[-1] - 1
            ans += bounded_height * horizontal_index_distance 

        stack.append(cur_i)  # If the bar is going down, we push it to the stack
        cur_i += 1
    return ans
```
## HOLLY TWO POINTERS
以對方為無限高牆輪流做梯田
```python=
class Solution:
    def trap(self, height: List[int]) -> int:
        L = 0
        R = len(height) - 1
        Lmax = 0
        Rmax = 0
        ans = 0
        while L < R:
            if height[L] < height[R]:
                if height[L] > Lmax:
                    Lmax = height[L]
                else:
                    ans += Lmax - height[L]
                L += 1
            else:
                if height[R] > Rmax:
                    Rmax = height[R]
                else:
                    ans += Rmax - height[R]
                R -= 1
        return ans    
```