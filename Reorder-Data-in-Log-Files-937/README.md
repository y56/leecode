# 937. Reorder Data in Log Files

:::info
To write a tuple containing a single value you have to include a comma, even though there is only one value
```python=
tup1 = (50,)
```
york: make sense. otherwise we will confuse between `(50,)` and `(50)`
:::

```python=
class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        
        def f(log):
            id_, rest = log.split(" ", 1)  # use " " to split once
            if rest[0].isalpha():  # if it is a letter-log
                return (0, rest, id_)  # use content to sort, if the same, use id_ to sort
            else:  # if it is a digit-log
                return (1,)  # Digit-logs come after letter-logs, being in-place
        
        return sorted(logs, key = f)

```

## empty is smaller

```python=
sorted([(), (1,)])
[(), (1,)]

sorted([(1,), ()])
[(), (1,)]
```
```python=
sorted([('a',), ()])
[(), ('a',)]

sorted([(), ('a',)])
[(), ('a',)]
```

