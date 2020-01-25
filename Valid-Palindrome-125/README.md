# 125. Valid Palindrome
##  
https://stackoverflow.com/questions/265960/best-way-to-strip-punctuation-from-a-string
### translate()
```python=
import string
class Solution:
    def isPalindrome(self, s: str) -> bool:
        translation_table = str.maketrans('', '', string.punctuation)
        no_punctuation = s.translate(translation_table)
        no_space_all_lower = no_punctuation.replace(' ', '').lower()
        if no_space_all_lower == no_space_all_lower[::-1]:
            return True
        return False
```
### set() 
```python=
import string
class Solution:
    def isPalindrome(self, s: str) -> bool:
        exclude = set(string.punctuation)
        no_punctuation = ''.join(ch for ch in s if ch not in exclude)
        no_space_all_lower = no_punctuation.replace(' ', '').lower()
        if no_space_all_lower == no_space_all_lower[::-1]:
            return True
        return False
```
### set() faster
```python=
import string
class Solution:
    def isPalindrome(self, s: str) -> bool:
        exclude = set(string.punctuation)
        no_punctuation = ''.join([ch for ch in s if ch not in exclude])
        no_space_all_lower = no_punctuation.replace(' ', '').lower()
        if no_space_all_lower == no_space_all_lower[::-1]:
            return True
        return False
```
### replace()
```python=
import string
class Solution:
    def isPalindrome(self, s: str) -> bool:
        for c in string.punctuation:
            s = s.replace(c, '')
        no_space_all_lower = s.replace(' ', '').lower()
        if no_space_all_lower == no_space_all_lower[::-1]:
            return True
        return False
```
### regular expression
reg_ex
```python=
import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        regex = re.compile('[%s]' % re.escape(string.punctuation))
        no_punctuation = regex.sub('', s)
        no_space_all_lower = no_punctuation.replace(' ', '').lower()
        if no_space_all_lower == no_space_all_lower[::-1]:
            return True
        return False
```
## isalnum()
```python=
class Solution:
    def isPalindrome(self, s):
        s = ''.join(c for c in s if e.isalnum()).lower()
        return s==s[::-1]
```