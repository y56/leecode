class TreeNode():
    def __init__(self):
        self.dict={}
        self.is_end_of_word=False
class Trie:
    def __init__(self):
        self.root = TreeNode()
    def insert(self, word: str) -> None:
        cur=self.root
        for c in word:
            tmp_dict = cur.dict
            if c in tmp_dict:
                cur=tmp_dict[c]
            else:
                tmp_dict[c] = TreeNode()
                cur=tmp_dict[c]
        cur.is_end_of_word=True
    def search(self, word: str) -> bool:
        cur=self.root
        for c in word:
            if c in cur.dict:
                cur=cur.dict[c]
            else:
                return False
        return cur.is_end_of_word
    def startsWith(self, prefix: str) -> bool:
        cur=self.root
        for c in prefix:
            if c in cur.dict:
                cur=cur.dict[c]
            else:
                return False
        return True
# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
class TreeNode():
    def __init__(self):
        self.dict=defaultdict(TreeNode)
        self.is_end_of_word=False
class Trie:
    def __init__(self):
        self.root = TreeNode()
    def insert(self, word: str) -> None:
        cur=self.root
        for c in word:
            cur = cur.dict[c]
        cur.is_end_of_word=True
    def search(self, word: str) -> bool:
        cur=self.root
        for c in word:
            if c in cur.dict:
                cur=cur.dict[c]
            else:
                return False
        return cur.is_end_of_word
    def startsWith(self, prefix: str) -> bool:
        cur=self.root
        for c in prefix:
            if c in cur.dict:
                cur=cur.dict[c]
            else:
                return False
        return True
