# 69. Sqrt(x)
## squeeze
For$$x >= 4$$
We have
$$\sqrt x >= 2$$
Then,
$$\sqrt x * \sqrt x >= 2 * \sqrt x$$
So, the upper bound is
$$\sqrt x =< x/2$$
From $x > 4$, the lower bound is
$$2 =< \sqrt x$$
So,
$$2 =< \sqrt x =< x/2$$
Taking floor
$$floor(2) <= floor(\sqrt x) <= floor(x/2)$$

```python=
class Solution:
    def mySqrt(self, x):
        if x == 0: return 0
        if x < 4: return 1
        
        # x >= 4
        l = 2 # left ptr of sqrt x
        r = x // 2 # right ptr of sqrt x
        # Note that, 
        # l**2 and r**2 will be both larger than x 
        # during the alfor x=6,7,8
        while r >= l:
            m = (l + r) // 2 
            m2 = m ** 2
            if m2 > x:
                r = m - 1
            elif m2 < x:
                l = m + 1
            else: # == # we hit it!
                return m
        return r
```

```
In the second last execution of while,   
l is n and r is be n+1  
i.e., (l,r) are (n,n+1)  

obviously, we want n  

and then m will be n  
but n^2 < x  
so m2 < x  
then l will be m+1 which is n+1  
now (l,r) are (n+1,n+1)  

In the last execution of while,  

l is n+1 and r is n+1  
and m will be n+1  
then m2 > x  
the new r will be m-1 which is n  
now, (l,r) are (n+1,n)   
can't enter the while-loop  
```
Actually, the second last is not always (l,r)=(n, n+1)  
However, we are always leaving while-loop by (n+1,n)