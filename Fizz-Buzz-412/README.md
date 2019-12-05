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
## 