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
## .most_common(1)
```python=
class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        
        banset = set(banned)
        
        for c in "!?',;.":
            paragraph = paragraph.replace(c, " ")
        
        word_list = paragraph.lower().split()
        
        count = collections.Counter(word for word in word_list if word not in banset)
        
        return count.most_common(1)[0][0]
```

```python=
class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        
        banset = set(banned)
        
        for c in "!?',;.":
            paragraph = paragraph.replace(c, " ")
        
        word_list = paragraph.lower().split()
                
        count = collections.Counter()
        for word in word_list :
            if word not in banset:
                count[word] += 1
        
        return count.most_common(1)[0][0]
```
## regular expression magic
```python=
def mostCommonWord(self, p, banned):
    ban = set(banned)
    words = re.findall(r'\w+', p.lower())
    return collections.Counter(w for w in words if w not in ban).most_common(1)[0][0]
```
```python=
def mostCommonWord(self, p, banned):
    ban = set(banned)
    words = re.sub(r'[^a-zA-Z]', ' ', p).lower().split()
    return collections.Counter(w for w in words if w not in ban).most_common(1)[0][0]
```
```python=
def mostCommonWord(self, paragraph, banned):
    tokens = [token for token in re.findall(r"([a-zA-Z]+)",  paragraph.lower()) if token not in banned]
    mostComm = collections.Counter(tokens).most_common(1)
    return mostComm[0][0]
```