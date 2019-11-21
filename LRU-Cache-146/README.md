# 146. LRU Cache

## OOP in python
ref = https://www.w3schools.com/python/python_inheritance.asp

## OrderedDict

:::information
```
result.popitem(last=False)
```
`OrderedDict.popitem()` returns the first or last key-value, after deleting it. 

Setting `last` to `False` signals you wanted to remove the first. 
:::

```python=
from collections import OrderedDict

class LRUCache(OrderedDict):  # inheritance

    def __init__(self, capacity: int):
        
        self.capacity = capacity

    def get(self, key: int) -> int:
        
        if key not in self:
            return-1
        
        self.move_to_end(key)  # update its usage status
        return self[key]
        
    def put(self, key: int, value: int) -> None:
        
        if key in self:
            self.move_to_end(key)  # update its usage status
        
        self[key] = value  # if key was in OrderedDict, it has been move_to_end
        # if key isn't in OrderedDict, it will be attached to the end
        
        if len(self) > self.capacity:
            self.popitem(last = False)  # `last = False` signals deleting the first not the last
        

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

```

