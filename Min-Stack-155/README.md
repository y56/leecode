# 155. Min Stack
```python=
# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
```
## less space
When push(x),  
if x is a new min,  
set x as new_min
and push  
$(new\text{_}min - (old\text{_}min - new\text{_}min)) = 2*new\text{_}min - old\text{_}min$  
to the stack

When getmin(),  
if the top of the stack is smaller than the min,  
then min is the min.

When pop(),  
if the top is smaller than min,  
we have to retrieve the previous min,  
$previous\text{_}min = cur\text{_}min + (cur\text{_}min - top$)
```python=
class MinStack:

    def __init__(self):
        self.stack = []
        self.min = None
        
    def push(self, x: int) -> None:
        if self.min == None:
            self.min = x
            self.stack.append(x)
        else:
            if x < self.min:
                self.stack.append(x - (self.min - x)) 
                # x - (cur_min - x) is surely smaller than x
                self.min = x
            else:
                self.stack.append(x)

    def pop(self) -> None:
        if self.stack == []:
            return
        if self.stack[-1] < self.min:
            # recover the previous min
            self.min = self.min + (self.min - self.stack.pop())
        else:
            self.stack.pop()
            if self.stack == []:
                self.min = None

    def top(self) -> int:
        if self.stack == []:
            return
        if self.stack[-1] >= self.min:
            return self.stack[-1]
        return self.min

    def getMin(self) -> int:
        return self.min
```
## store every current min by tuples
- pros
    - less memory
    - you can use tuples in a dictionary, as a key. While you can't do so with a list.
- cons
    - immutable
        * You can't add an element but in a list you can 
        * You can't sort a tuple but in a list you can 
        * You can't delete an element but you can in a list 
        * You can't replace an element but you can in a list

```python=
class MinStack:

    def __init__(self):
        self.stack = []
        
    def push(self, x: int) -> None:
        if self.stack == [] or x < self.stack[-1][1]:
            self.stack.append((x, x))
        else:
            self.stack.append((x, self.stack[-1][1]))

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        if self.stack == []:
            return None
        return self.stack[-1][0]

    def getMin(self) -> int:
        if self.stack == []:
            return None
        return self.stack[-1][1]
```
