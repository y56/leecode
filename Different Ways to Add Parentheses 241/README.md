# 241. Different Ways to Add Parentheses
## recursive
No memory, bad.
```python=
class Solution:
  def diffWaysToCompute(self, input: str) -> List[int]:

    if input.isnumeric():
      return [input]
    
    res = []
    
    for ind, ch in enumerate(input):
      if ch == '+':
        def func(a,b): return int(a)+int(b)
      elif ch == '-':
        def func(a,b): return int(a)-int(b)
      elif ch == '*':
        def func(a,b): return int(a)*int(b)
      else:
        continue
      
      str1 = input[:ind]
      str2 = input[ind+1:]
      res1 = self.diffWaysToCompute(str1) # have to use `self.` !!
      res2 = self.diffWaysToCompute(str2)
      
      
      for num1 in res1:
        for num2 in res2:
          res.append(func(num1, num2))
          
    return res
```

## recursive but w/ a global dict as a dp chart
```python=
def diffWaysToCompute(self, input: str) -> List[int]:

    def helper(input):
        if input.isnumeric():
            return [input]

        if input in d:
            # print(input)
            return d[input]

        res = []
        # ct.append(1)
        for ind, ch in enumerate(input):
            if ch == '+':
                def func(a,b): return int(a)+int(b)
            elif ch == '-':
                def func(a,b): return int(a)-int(b)
            elif ch == '*':
                def func(a,b): return int(a)*int(b)
            else:
                continue

            str1 = input[:ind]
            str2 = input[ind+1:]
            res1 = helper(str1)
            res2 = helper(str2)


            for num1 in res1:
                for num2 in res2:
                    res.append(func(num1, num2))

        d.update({input:res}) # You can't d.update(input=res) # that is for str "input"
        return res

    d = {}

    return helper(input)
```
### 
```python=
class Solution:
    def diffWaysToCompute(self, input: str) -> List[int]:
        
        
        def helper(input):
            if input.isnumeric():
                return [int(input)]

            if input in d:
                return d[input]

            res = []
            for ind, ch in enumerate(input):
                if ch == '+':
                    def func(a,b): return a+b
                elif ch == '-':
                    def func(a,b): return a-b
                elif ch == '*':
                    def func(a,b): return a*b
                else:
                    continue

                str1 = input[:ind]
                str2 = input[ind+1:]
                res1 = helper(str1)
                res2 = helper(str2)


                for num1 in res1:
                    for num2 in res2:
                        res.append(func(num1, num2))

            d.update({input:res}) # You can't d.update(input=res) # that is for str "input"
            return res

        d = {}

        return helper(input)
```
### 
```python=
class Solution:
    def diffWaysToCompute(self, input: str) -> List[int]:
        
        d = {}
        
        operation_dict = {'+': lambda a,b:a+b, 
                          '-': lambda a,b:a-b,
                          '*': lambda a,b:a*b}
        
        def helper(input):
            if input.isnumeric():
                return [int(input)]

            if input in d:
                return d[input]

            res = []
            for ind, ch in enumerate(input):
                
                if ch not in operation_dict:
                    continue
                func = operation_dict[ch]

                str1 = input[:ind]
                str2 = input[ind+1:]
                res1 = helper(str1)
                res2 = helper(str2)

                for num1 in res1:
                    for num2 in res2:
                        res.append(func(num1, num2))

            d.update({input:res}) # You can't d.update(input=res) # that is for str "input"
            return res

        return helper(input)
```