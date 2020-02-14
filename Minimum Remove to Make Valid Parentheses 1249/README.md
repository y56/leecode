###### tags: `leetcode`

# 1249. Minimum Remove to Make Valid Parentheses
```python=
def minRemoveToMakeValid(self, s: str) -> str:
    stack = []
    ind_to_del = set()
    for i, ele in enumerate(s):
        if ele == '(':
            stack.append((i)) 
            # every ele in stack is an index of a '('
        if ele == ')':
            if stack:
                stack.pop()
            else:
                ind_to_del.add(i)
    for ele in stack: 
    # these are indices of unpaired '('
        ind_to_del.add(ele)
    string_builder = []
    for i, ele in enumerate(s):
        if i not in ind_to_del:
            string_builder.append(ele)
    return ''.join(string_builder)
```
## two parse
```python=
def minRemoveToMakeValid(self, s: str) -> str:
    li = []
    count = 0
    for ch in s:
        if ch == '(':
            count += 1
        if ch == ')':
            if count == 0:
                continue
            else:
                count -= 1
        li.append(ch)
    count = 0
    i = len(li) - 1
    while i >= 0:
        ch = li[i]
        if ch == ')':
            count += 1
        if ch == '(':
            if count == 0:
                del li[i]  
                # !!! can't use li.remove(ele)
                # li.remove(ele) if for ele not index
            else:
                count -= 1
        i -= 1
    return ''.join(li)
```
## two parse, make function to reuse
```python=
def minRemoveToMakeValid(self, s: str) -> str:
    def delete_invalid_closing(string, open_symbol, close_symbol):
        list_ = []
        count = 0
        for ch in string:
            if ch == open_symbol:
                count += 1
            if ch == close_symbol:
                if count == 0:
                    continue
                else:
                    count -= 1
            list_.append(ch)
        return ''.join(list_)

    no_extra_right_parentheses = delete_invalid_closing(s, '(', ')')
    no_extra_left_parentheses = delete_invalid_closing(no_extra_right_parentheses[::-1], ')', '(')

    return no_extra_left_parentheses[::-1]
```
