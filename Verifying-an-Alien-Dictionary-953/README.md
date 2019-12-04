# 953. Verifying an Alien Dictionary
## me
### Highlight
#### to create a dictionary 
:::info
```python=
mydict = {char: count for count, char in enumerate(order)}
```
**is the same as**
```python=
mydict = {}
for count, char in enumerate(order):
   mydict.update({char: count})
```
:::
#### zip ignores the un-matching part
:::info
```python=
for c1,c2 in zip(word1,word2):  
```
**zip stops when one of them is used up**

:::


```python=
class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:

        mydict = {char: count for count, char in enumerate(order)}
        
        def compare(word1, word2, mydict):
            needtocomparelen = True
            for c1,c2 in zip(word1,word2):  # zip stops when one of them is used up 
                if mydict[c1] > mydict[c2]:
                    return False
                elif mydict[c1] < mydict[c2]:
                    needtocomparelen = False 
                    break
            
            if needtocomparelen and len(word1) > len(word2):
                return False
            return True
        
        for word1, word2 in zip(words[:-1], words[1:]):
            if False == compare(word1, word2, mydict):
                return False
        return True
```

## me, revised
By not using internal function, the `return False` can directly end the process.
```python=
class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:

        mydict = {char: count for count, char in enumerate(order)}
        
        for word1, word2 in zip(words[:-1], words[1:]):
            
            needtocomparelen = True
            for c1,c2 in zip(word1,word2):  # zip stops when one of them is used up 
                if mydict[c1] > mydict[c2]:
                    return False
                elif mydict[c1] < mydict[c2]:
                    needtocomparelen = False 
                    break
            
            if needtocomparelen and len(word1) > len(word2):
                return False

        return True
```
## solution
### for-else
:::info
There exist ***for-else*** and ***while-else***.
:::
:::info
https://intoli.com/blog/for-else-in-python/
:::
```python=
class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        order_index = {c: i for i, c in enumerate(order)}

        for i in range(len(words) - 1):
            word1 = words[i]
            word2 = words[i+1]

            # Find the first difference word1[k] != word2[k].
            for k in range(min(len(word1), len(word2))):
                # If they compare badly, it's not sorted.
                if word1[k] != word2[k]:
                    if order_index[word1[k]] > order_index[word2[k]]:
                        return False
                    break
            else:
                # If we didn't find a first difference, the
                # words are like ("app", "apple").
                if len(word1) > len(word2):
                    return False

        return True
```