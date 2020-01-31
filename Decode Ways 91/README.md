# 91. Decode Ways
## me, wrong strategy, fail
### try 1, fail
```python=
class Solution:
    def numDecodings(self, s: str) -> int:
        ints = int(s)
        if       ints == 0:  return 0
        if  1 <= ints <= 10: return 1
        if 11 <= ints <= 19: return 2
        if       ints == 10: return 1
        if 21 <= ints <= 26: return 2
        if 27 <= ints <= 99: return 1
        return self.numDecodings(s[0:2]) * self.numDecodings(s[2:]) + self.numDecodings(s[0]) * self.numDecodings(s[1:])
        
```
:::danger
Wrong Answer

Input
"226"

Output
4

Expected
3
:::
I double count the `2 | 2 | 6`
### try 2, fail
```python=
class Solution:
    def numDecodings(self, s: str) -> int:
        ints = int(s)
        if       ints == 0:  return 0
        if  1 <= ints <= 10: return 1
        if 11 <= ints <= 19: return 2
        if       ints == 10: return 1
        if 21 <= ints <= 26: return 2
        if 27 <= ints <= 99: return 1
        return self.numDecodings(s[0:2]) * self.numDecodings(s[2:]) + self.numDecodings(s[0]) * self.numDecodings(s[1:]) - self.numDecodings(s[0]) * self.numDecodings(s[1]) * self.numDecodings(s[2:])
```
:::danger
Wrong Answer

Input
"01"

Output
1

Expected
0
:::
`"01"` is going the same as `"1"`, which is wrong
### try 3, fail
```python=
class Solution:
    def numDecodings(self, s: str) -> int:
        if len(s) ==  2 and s[0] == "0":
            return 0
        ints = int(s)
        if       ints == 0:  return 0
        if  1 <= ints <= 10: return 1
        if 11 <= ints <= 19: return 2
        if       ints == 10: return 1
        if 21 <= ints <= 26: return 2
        if 27 <= ints <= 99: return 1
        return self.numDecodings(s[0:2]) * self.numDecodings(s[2:]) + self.numDecodings(s[0]) * self.numDecodings(s[1:]) - self.numDecodings(s[0]) * self.numDecodings(s[1]) * self.numDecodings(s[2:]) 
```
:::danger
Wrong Answer

Input
"012"

Output
2

Expected
0
:::
### try 4, fail
```python=
class Solution:
    def numDecodings(self, s: str) -> int:
        if s[0] == "0":
            return 0
        ints = int(s)
        if       ints == 0:  return 0
        if  1 <= ints <= 10: return 1
        if 11 <= ints <= 19: return 2
        if       ints == 10: return 1
        if 21 <= ints <= 26: return 2
        if 27 <= ints <= 99: return 1
        return self.numDecodings(s[0:2]) * self.numDecodings(s[2:]) + self.numDecodings(s[0]) * self.numDecodings(s[1:]) - self.numDecodings(s[0]) * self.numDecodings(s[1]) * self.numDecodings(s[2:])
```
:::danger
Wrong Answer

Input
"230"

Output
1

Expected
0
:::
### try 5, fail
```python=
class Solution:
    def numDecodings(self, s: str) -> int:
        if s[0] == "0":
            return 0
        ints = int(s)
        if       ints == 0:  return 0
        if  1 <= ints <= 10: return 1
        if 11 <= ints <= 19: return 2
        if       ints == 10: return 1
        if 21 <= ints <= 26: return 2
        if ints == 30 or ints == 40 or ints == 50 or ints == 60 or ints == 70 or ints == 80 or ints == 90: return 0
        if 27 <= ints <= 99: return 1
        return self.numDecodings(s[0:2]) * self.numDecodings(s[2:]) + self.numDecodings(s[0]) * self.numDecodings(s[1:]) - self.numDecodings(s[0]) * self.numDecodings(s[1]) * self.numDecodings(s[2:])
```

:::danger
Runtime Error
Details
Playground Debug
RecursionError: maximum recursion depth exceeded while calling a Python object
Line 3 in numDecodings (Solution.py)
  [Previous line repeated 996 more times]
Line 14 in numDecodings (Solution.py)
Line 14 in numDecodings (Solution.py)
Line 14 in numDecodings (Solution.py)
stdout
12120
12
120
12
0
1
20
20
20
20
20
20
20

... 49910 more lines
Last executed input
"12120"
:::
It is a typo.
Should be  
`if       ints == 10: return 1`
Not  
`if       ints == 20: return 1`
### try 6, fail
```python=
class Solution:
    def numDecodings(self, s: str) -> int:
        print(s)
        if s[0] == "0":
            return 0
        ints = int(s)
        if       ints == 0:  return 0
        if  1 <= ints <= 10: return 1
        if 11 <= ints <= 19: return 2
        if       ints == 20: return 1
        if 21 <= ints <= 26: return 2
        if ints == 30 or ints == 40 or ints == 50 or ints == 60 or ints == 70 or ints == 80 or ints == 90: return 0
        if 27 <= ints <= 99: return 1
        return self.numDecodings(s[0:2]) * self.numDecodings(s[2:]) + self.numDecodings(s[0]) * self.numDecodings(s[1:]) - self.numDecodings(s[0]) * self.numDecodings(s[1]) * self.numDecodings(s[2:])
```
:::danger
Time Limit Exceeded

Last executed input

"6065812287883668764831544958683283296479682877898293612168136334983851946827579555449329483852397155"
:::
### try 7, fail
```python=
class Solution:
    def numDecodings(self, s: str) -> int:
        if s[0] == "0":
            return 0
        ints = int(s)
        if       ints == 0:  return 0
        if  1 <= ints <= 10: return 1
        if 11 <= ints <= 19: return 2
        if       ints == 20: return 1
        if 21 <= ints <= 26: return 2
        if ints == 30 or ints == 40 or ints == 50 or ints == 60 or ints == 70 or ints == 80 or ints == 90: return 0
        if 27 <= ints <= 99: return 1
        return (self.numDecodings(s[0:2]) - self.numDecodings(s[0])*self.numDecodings(s[1]))*self.numDecodings(s[2:]) + self.numDecodings(s[0])*self.numDecodings(s[1:]) 
```
:::danger
Time Limit Exceeded

Last executed input

"6065812287883668764831544958683283296479682877898293612168136334983851946827579555449329483852397155"

:::
:::info
I shoud have memory  
I should DP
:::

## dp
### try 1, fail
```python=
class Solution:
    def numDecodings(self, s: str) -> int:
        if s[0] == "0":
            return 0
        
        # the first char is not '0'
        n = len(s)
        dp = [0] * n # 0 ~ n-1
        dp[0] = 1
        for i in range(1, n):
            if s[i] != '0':
                dp[i] = dp[i-1]
            if 10 <= int(s[i-1:i+1]) <= 26: # i-1 ~ i
                dp[i] += 1
        return dp[-1]
```
:::danger
Wrong Answer

Input
"12120"
Output
1
Expected
3
:::
### try 2, success, use `if` in `for` to deal with the special case of counting `s[0:3]`
```python=
class Solution:
    def numDecodings(self, s: str) -> int:
        if s[0] == "0":
            return 0
        
        # the first char is not '0'
        n = len(s)
        dp = [0] * n # 0 ~ n-1
        dp[0] = 1
        for i in range(1, n):
            print(dp)
            if s[i] != '0':
                dp[i] += dp[i-1]
            if 10 <= int(s[i-1:i+1]) <= 26: # i-1 ~ i
                # to avoid access of dp[-1]
                if i == 1 :
                    dp[i] += 1
                else:
                    dp[i] += dp[i-2]
        print(dp)
        return dp[-1]
```
### try 3, success, shift dp chart to avoid  `dp[0:3]`
```python=
class Solution:
    def numDecodings(self, s: str) -> int:
        if s[0] == "0":
            return 0
        
        # the first char is not '0'
        n = len(s)
        dp = [0] * (n+1) # 0 ~ n
        # we shift the dp chart from the input s by 1
        
        # the possible decode way of s[0:a+1] is stroe at dp[a+1]
        dp[0] = 1 # only for counting the 2-digit at s[0~1], 
        dp[1] = 1 # for the first char is not '0', there is one decode way
        
        for i in range(2, n+1):
            
            # if the 1-digit is 1~9 then the previous count is OK to use
            if s[i-1] != '0':
                dp[i] += dp[i-1]
            
            # if the 2-digit is 10~26, then the previous count is OK to use
            if 10 <= int(s[i-2:i]) <= 26:
                dp[i] += dp[i-2]
        
        return dp[n]
```
