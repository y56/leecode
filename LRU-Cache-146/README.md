# 146. LRU Cache

## OOP in python
ref = https://www.w3schools.com/python/python_inheritance.asp

### parent class
```python=
class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname
```
### inherit but change nothing
```python=
 class Student(Person):
     pass 
```
### override
```python=
class Student(Person):
    def __init__(self, fname, lname):
```
### override but also pass parameters to parent's constructor
```python=
class Student(Person):
    def __init__(self, fname, lname):
        super().__init__(fname, lname)  # same as Person.__init__(fname, lname)
        self.graduationyear = 2019
```


## OrderedDict in pyhon

:::info
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

## Hashmap + DoubleLinkedList

One advantage of ***double linked list*** is that the node can remove itself without other reference. 

If it is a single linked list, we can't remove a certain node given by a hash-map. We have to start from the head of the list to find the previous node of this node if it is a single linked list

```python=
class DLinkedNode(): 
    def __init__(self):
        self.key = 0
        self.value = 0
        self.prev = None
        self.next = None
            
class LRUCache():
    def _add_node(self, node):
        """
        Always add the new node right after head.
        """
        node.prev = self.head
        node.next = self.head.next

        self.head.next.prev = node
        self.head.next = node

    def _remove_node(self, node):
        """
        Remove an existing node from the linked list.
        """
        prev = node.prev
        new = node.next

        prev.next = new
        new.prev = prev

    def _move_to_head(self, node):
        """
        Move certain node in between to the head.
        """
        self._remove_node(node)
        self._add_node(node)

    def _pop_tail(self):
        """
        Pop the current tail.
        """
        res = self.tail.prev
        self._remove_node(res)
        return res

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.cache = {}
        self.size = 0
        self.capacity = capacity
        self.head, self.tail = DLinkedNode(), DLinkedNode()

        self.head.next = self.tail
        self.tail.prev = self.head
        

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        node = self.cache.get(key, None)  
        # Use `None`, it will return `None` when not found
        if not node:
            return -1

        # move the accessed node to the head;
        self._move_to_head(node)

        return node.value

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        node = self.cache.get(key)  # note that self.cache = {}

        if not node: 
            newNode = DLinkedNode()
            newNode.key = key
            newNode.value = value

            self.cache[key] = newNode
            self._add_node(newNode)

            self.size += 1

            if self.size > self.capacity:
                # pop the tail
                tail = self._pop_tail()
                del self.cache[tail.key]
                self.size -= 1
        else:
            # update the value.
            node.value = value
            self._move_to_head(node)
            
```