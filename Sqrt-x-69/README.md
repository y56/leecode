# 69. Sqrt(x)
## best, remember this one
```python=
class Solution:
    def mySqrt(self, x):
        l, r = 0, x
        while l <= r:
            mid = (r+l)//2
            if mid * mid <= x < (mid+1)*(mid+1):
                return mid
            elif x < mid * mid:
                r = mid
            else:
                l = mid + 1
```
## Newton's; fastest

![](https://i.imgur.com/0z2DKi4.jpg)


https://en.wikipedia.org/wiki/Integer_square_root#Digit-by-digit_algorithm

Note that since we choose the first guess as x, the next guess is always smaller or equal to the previous guess.

As long as we start Newton's method from a guess larger than sqrt(x), the guess is always decreasing.

Once the int(guess) is <= x, it is the ans

In Newton's method, we will never go to somewhere smaller than sqrt(x) for float method.

In Newton's method, we will never go to somewhere smaller than floor(sqrt(x)) for int method.

### having float, comparing with input, REMEMBER

```python=
class Solution:
    def mySqrt(self, x):
        guess = x
        # we don't have to check that much 
        # while not(int(guess)**2 <= x < (int(guess)+1)**2):
        # we only have to check
        while int(guess)**2 > x:
            guess = (guess + x / guess) / 2        
            
        return int(guess)
```
### all int, comparing with input, REMEMBER
```python=
class Solution:
    def mySqrt(self, x):
        guess = x
        while guess**2 > x:
            guess = (guess + x // guess) // 2  # it's an int
            
        return guess
```
### by differenc between guesses, use float
https://en.wikipedia.org/wiki/Integer_square_root#Stopping_criterion
```python=
class Solution:
    def mySqrt(self, x):
        if x < 2:
            return x
        
        cur_guess = x
        next_guess = (cur_guess + x / cur_guess) / 2
        while abs(cur_guess - next_guess) >= 1: 
        # a little bit danger, since using float
        # https://en.wikipedia.org/wiki/Integer_square_root#Stopping_criterion
            cur_guess = next_guess
            next_guess = (cur_guess + x / cur_guess) / 2        
            
        return int(next_guess)
```
### by differenc between guesses, all int
![](https://i.imgur.com/5VgVven.png)

```python=
class Solution:
    def mySqrt(self, x):
        if x < 2:
            return x
        
        cur_guess = x
        next_guess = (cur_guess + x // cur_guess) // 2
        
        # go in if stricly decreasing
        while cur_guess - next_guess > 0: 
        # while not((cur_guess - next_guess) == -1 or cur_guess == next_guess):
        
        # https://en.wikipedia.org/wiki/Integer_square_root#Stopping_criterion
            
            cur_guess = next_guess
            next_guess = (cur_guess + x // cur_guess) // 2        
            
        return cur_guess
```
## squeeze
For
$$x >= 4$$
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
        # l**2 and r**2 will be both >= than x 
        # during the algorithm for all x >= 4
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

Actually, the second last is not always `(l,r)=(n, n+1)  `
However, we are always leaving while-loop by `(l,r) = (n+1,n)`

## Recursion + Bit Shifts

A fact is that 
$$ sqrt(x) = 2 * sqrt(x/4) $$
and
$$ floor(sqrt(x)) = 2 * floor(sqrt(x/4)) $$

We can set the base cases as 
```
my_sqrt(3) = 1
my_sqrt(2) = 1
my_sqrt(1) = 1
my_sqrt(0) = 0
```

But we can't put x/4 into my_sqrt,  
we need to do something. but i don't know...

```python=
class Solution:
    def mySqrt(self, x):
        if x<0: return None
        if x == 0: return 0
        if x < 4: return 1
        
        left = 2 * self.mySqrt(x // 4)
        right = left + 1
        if right ** 2 > x:
            return left
        else:  # right ** 2 <= x
            return right
```

Okay, I don't know why there are left and right.

