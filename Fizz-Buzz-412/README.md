###### tags: `leetcode`
# 412. Fizz Buzz
## my first try
```python=
class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        #  3 Fizz
        #  5 Buzz
        # 15 FizzBuzz
        ans = []
        for i in range(1, n+1):
            if i / 15 == i // 15 :
                ans.append("FizzBuzz")
            else:
                if i / 3 == i // 3 :
                    ret.append("Fizz")
                elif i / 5 == i // 5 :
                    ret.append("Buzz")
                else:
                    ret.append(str(i))
        return ans
``` 
Time Complexity: O(N)O(N)O(N)  
Space Complexity: O(1)O(1)O(1)
## use `%` and `elif`
```python=
class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        ans = []
        for i in range(1, n+1):
            divisible_by_3 = (i % 3 == 0)
            divisible_by_5 = (i % 5 == 0)
            if divisible_by_3 and divisible_by_5:
                ans.append("FizzBuzz")
            elif divisible_by_3:
                ans.append("Fizz")
            elif divisible_by_5:
                ans.append("Buzz")
            else:
                ans.append(str(i))
        return ans
```
Time Complexity: O(N)O(N)O(N)  
Space Complexity: O(1)O(1)O(1)
## String Concatenation

If you try to solve this with the previous approach the program would have too many conditions to check:
:::success
3 ---> "Fizz" , 5 ---> "Buzz", 7 ---> "Jazz"
:::
    Divisible by 3
    Divisible by 5
    Divisible by 7
    Divisible by 3 and 5
    Divisible by 3 and 7
    Divisible by 7 and 3
    Divisible by 3 and 5 and 7
    Not divisible by 3 or 5 or 7.
```
Condition 1: 15 % 3 == 0 , num_ans_str = "Fizz"
Condition 2: 15 % 5 == 0 , num_ans_str += "Buzz"
=> num_ans_str = "FizzBuzz"
```

```python=
class Solution:
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        # ans list
        ans = []

        for num in range(1,n+1):

            divisible_by_3 = (num % 3 == 0)
            divisible_by_5 = (num % 5 == 0)

            num_ans_str = ""

            if divisible_by_3:
                # Divides by 3
                num_ans_str += "Fizz"
            if divisible_by_5:
                # Divides by 5
                num_ans_str += "Buzz"
            if not num_ans_str:
                # Not divisible by 3 or 5
                num_ans_str = str(num)

            # Append the current answer str to the ans list
            ans.append(num_ans_str)  

        return ans
```

Time Complexity: O(N)O(N)O(N)  
Space Complexity: O(1)O(1)O(1)

## Hash it!

```python=
class Solution:
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        # ans list
        ans = []

        # Dictionary to store all fizzbuzz mappings
        fizz_buzz_dict = {3 : "Fizz", 5 : "Buzz"}

        for num in range(1,n+1):

            num_ans_str = ""

            for key in fizz_buzz_dict.keys():

                # If the num is divisible by key,
                # then add the corresponding string mapping to current num_ans_str
                if num % key == 0:
                    num_ans_str += fizz_buzz_dict[key]

            if not num_ans_str:
                num_ans_str = str(num)

```
Time Complexity : O(N)O(N)O(N)  
Space Complexity : O(1)O(1)O(1)