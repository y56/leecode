# 819. Most Common Word
## me, wrong
Can't handle this.
`"a, a, a, a, b,b,b,c, c"`
There are punctuations without space.

```python=
class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        for p in string.punctuation:
            paragraph = paragraph.replace(p,'')
        mylist = paragraph.lower().split(' ')
        c = collections.Counter(mylist)
        
        print(c)
        
        banned_set = set(banned)
        candidate_word = ''
        max_count = 0
        for word, count in c.items():
            print(word, count)
            if (count > max_count) and (word not in banned_set):
                candidate_word = word
                max_count = count
            print(candidate_word)
        return candidate_word
```
## me, ugly patch
```python=
class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        for p in string.punctuation:
            paragraph = paragraph.replace(p,' ') # !!!
        mylist = paragraph.lower().split(' ')
        c = collections.Counter(mylist)
        =
        c[''] = 0
        
        banned_set = set(banned)
        candidate_word = ''
        max_count = 0
        for word, count in c.items():
            print(word, count)
            if (count > max_count) and (word not in banned_set):
                candidate_word = word
                max_count = count
            print(candidate_word)
            
        return candidate_word
```
## should use just `split()` instead of `split(' ')` or `split('')`
```python=
class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        for p in string.punctuation:
            paragraph = paragraph.replace(p,' ')
        mylist = paragraph.lower().split()
        c = collections.Counter(mylist)
        
        banned_set = set(banned)
        candidate_word = ''
        max_count = 0
        for word, count in c.items():
            print(word, count)
            if (count > max_count) and (word not in banned_set):
                candidate_word = word
                max_count = count
            print(candidate_word)
            
        return candidate_word
```
## from others
```python=
class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        
        banset = set(banned)
        
        for c in "!?',;.":
            paragraph = paragraph.replace(c, " ")
        
        count = collections.Counter(paragraph.lower().split())
        
        ans, best_count = '', 0
        
        for word in count:
            if count[word] > best_count and word not in banset:
                ans, best = word, count[word]
                
        return ans
```
