###### tags: `leetcode`

# 20. Valid Parentheses

### Size

use `int` instead of `char` to in the stack
```python=
>>> sys.getsizeof(1)
28
>>> sys.getsizeof('a')
50
```

### Geometry Interpretation

- Let (, [, { stand for -x, -y, -z,
Let ), ], } stand for +x, +y, +z,

- Start from (0,0,0). End at (0,0,0).
- We can go toward -x/-y/-z or go back along the same path
    -  At (0,0,0), there is no previous path, so we can only go -x/-y/-z.
    -  Going back will erase the path.

## Stack Approach
Already good in space.
:::info
Runtime: 24 ms, faster than 97.46% of Python3 online submissions for Valid Parentheses.
Memory Usage: 12.6 MB, less than 100.00% of Python3 online submissions for Valid Parentheses.
:::
```python=
class Solution:
    def isValid(self, s: str) -> bool:

# three 1-dimensional walks
# No ! It is more complicated than three independent 1-dimensional walks.
# Note that "([)]" is illegal.
# This is a 3D walk.
# We can only proceed by x-=1 or y-=1 or z-=1.
# Or we can go back on the same path
        stack = []
        for char in s:

            # I use 1,2,3 instead of '(','[','{' because they 1,2,3 is smaller in size
            if '(' == char:
                stack.append(1)  
            if '[' == char:
                stack.append(2)  
            if '{' == char:
                stack.append(3)  
                
            if ')' == char:
                if stack:
                    if stack[-1] == 1:
                        stack.pop()
                    else:
                        return False
                else:
                    return False
            if ']' == char:
                if stack:
                    if stack[-1] == 2:
                        stack.pop()
                    else:
                        return False
                else:
                    return False
            if '}' == char:
                if stack:
                    if stack[-1] == 3:
                        stack.pop()
                    else:
                        return False
                else:
                    return False
                    
        if stack == []:
            return True
        else:
            return False
```
### Revision, using `elif` and `return stack==[]`
:::info
Runtime: 28 ms, faster than 91.84% of Python3 online submissions for Valid Parentheses.
Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Valid Parentheses..
:::
```python=
    def isValid(self, s: str) -> bool:
        stack = []
        for char in s:
            if '(' == char:
                stack.append(1)  
            if '[' == char:
                stack.append(2)  
            if '{' == char:
                stack.append(3)  
                
            if ')' == char:
                if stack == []:
                    return False
                elif stack[-1] == 1:
                    stack.pop()
                else:
                    return False
            if ']' == char:
                if stack == []:
                    return False
                elif stack[-1] == 2:
                    stack.pop()
                else:
                    return False
            if '}' == char:
                if stack == []:
                    return False
                elif stack[-1] == 3:
                    stack.pop()
                else:
                    return False
            
        return stack == []
```
### Further Revision, if the first condition fails, the second will not be judged
:::info
```python=
            if ')' == char:
                if stack == []:
                    return False
                elif stack[-1] == 1:
                    stack.pop()
                else:
                    return False
```
can be reduced to
```python=
            if ')' == char:
                if stack and stack[-1] == 1:
                    stack.pop()
                else:
                    return False```
:::
```python=
    def isValid(self, s: str) -> bool:
        stack = []
        for char in s:
            if '(' == char:
                stack.append(1)  
            if '[' == char:
                stack.append(2)  
            if '{' == char:
                stack.append(3)  
                
            if ')' == char:
                if stack and stack[-1] == 1:
                    stack.pop()
                else:
                    return False
            if ']' == char:
                if stack and stack[-1] == 2:
                    stack.pop()
                else:
                    return False
            if '}' == char:
                if stack and stack[-1] == 3:
                    stack.pop()
                else:
                    return False
            
        return stack == []
```

## Solution, `map {}`
A dummy element `'#'`
Easy to have more types of bracket.
```python=
class Solution(object):
    def isValid(self, s):
        # The stack to keep track of opening brackets.
        stack = []

        # Hash map for keeping track of mappings. This keeps the code very clean.
        # Also makes adding more types of parenthesis easier
        mapping = {")": "(", "}": "{", "]": "["}

        # For every bracket in the expression.
        for char in s:

            # If the character is an closing bracket
            if char in mapping:

                # Pop the topmost element from the stack, if it is non empty
                # Otherwise assign a dummy value of '#' to the top_element variable
                top_element = stack.pop() if stack else '#'

                # The mapping for the opening bracket in our hash and the top
                # element of the stack don't match, return False
                if mapping[char] != top_element:
                    return False
            else:
                # We have an opening bracket, simply push it onto the stack.
                stack.append(char)

        # In the end, if the stack is empty, then we have a valid expression.
        # The stack won't be empty for cases like ((()
        return not stack
```
## Concise
Though not very efficient.
```python=
class Solution(object):
    def isValid(self, s):
        while "()" in s or "{}" in s or '[]' in s:
            s = s.replace("()", "").replace('{}', "").replace('[]', "")
        return s == ''
```
## h2
`stack and i == bracket_map[stack[-1]]:`

```python=
class Solution(object):
    def isValid(self, s):
        bracket_map = {"(": ")", "[": "]",  "{": "}"}
        stack = []
        for i in s:
            if i in bracket_map:
                stack.append(i)
            elif stack and i == bracket_map[stack[-1]]:  # !!!
                    stack.pop()
            else:
                return False
        return stack == []
```