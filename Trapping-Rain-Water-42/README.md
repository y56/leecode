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