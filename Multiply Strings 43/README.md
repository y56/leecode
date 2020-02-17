# 43. Multiply Strings
```python=
class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        
        def add1dig(res, addant_1dig, pos):
            if addant_1dig == 0: 
                return
            
            add_res_1on1 = int(res[pos]) + addant_1dig
            
            res[pos] = str(add_res_1on1 % 10)
            
            if add_res_1on1 < 10:
                return
            else:
                add1dig(res, add_res_1on1 // 10, pos + 1) 
        
        res = ['0'] * (len(num1)+len(num2))
    
        for i in range(len(num2)): 
            for j in range(len(num1)): 
                
                prod_1on1 =  int(num2[~i]) * int(num1[~j])
                
                add1dig(res, prod_1on1 % 10, i + j)
                
                if prod_1on1 > 9:
                    add1dig(res, prod_1on1 // 10, i + j + 1)
                        
        while res and res[-1] == '0': 
            res.pop()
            
        if res == []: 
            return '0'
        
        return ''.join(res[::-1])
```
