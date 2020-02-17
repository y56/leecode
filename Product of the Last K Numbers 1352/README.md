# 1352. Product of the Last K Numbers
## my slow method
```python=
import numpy
class ProductOfNumbers:

    def __init__(self):
        self.li = []
        self.pli=[1]
        
    def add(self, num: int) -> None:
        self.li.append(num)
        if num:
            self.pli.append(self.pli[-1] * num)
        else:
            self.pli.append(self.pli[-1] * 1)

    def getProduct(self, k: int) -> int:
        if 0 in self.li[~0:~0-k:-1]:
            return 0
        return self.pli[-1] //  self.pli[-1 - k]
    
# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)
```
## smarter
```python=
class ProductOfNumbers:

    def __init__(self):
        self.accum_numof0 = [0] # accumulative_numof0_list
        self.accum_prod = [1]
        
    def add(self, num: int) -> None:
        if num == 0:
            self.accum_numof0.append(self.accum_numof0[-1] + 1)
            self.accum_prod.append(1) # if there comes a 0, reset the product
        else:
            self.accum_numof0.append(self.accum_numof0[-1])
            self.accum_prod.append(self.accum_prod[-1] * num)

    def getProduct(self, k: int) -> int:
        if self.accum_numof0[-1] > self.accum_numof0[-1 - k]:
        # there are some zeros in this range
            return 0
        return self.accum_prod[-1] //  self.accum_prod[-1 - k]
    
# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)
```

## so smart

Just as a zero is added, we can't get anything other than zero, so we reset everything.

```python=
class ProductOfNumbers:

    def __init__(self):
        self.accum_prod = [1]

    def add(self, num: int) -> None:
        if num == 0:
            self.accum_prod = [1] # reset !
        else:
            self.accum_prod.append(self.accum_prod[-1] * num)
        

    def getProduct(self, k: int) -> int:
# the number of non-zero `num`s since the last zero 
# is len(self.accum_prod)-1
# if you want more than that you will get 0
        if k > len(self.accum_prod) - 1 :
            return 0
        return self.accum_prod[-1] // self.accum_prod[-1 - k]

```
