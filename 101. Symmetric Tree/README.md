# 101. Symmetric Tree
## 
```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        # right first BFS
        q = [root]
        r_vals = []
        while q:
            if q[0]: 
                r_vals.append(q[0].val)
                q.append(q[0].right)
                q.append(q[0].left)
            else:
                r_vals.append(None)
            del q[0]
        # left first BFS
        q = [root]
        l_vals = []
        while q:
            if q[0]: 
                l_vals.append(q[0].val)
                q.append(q[0].left)
                q.append(q[0].right)
            else:
                l_vals.append(None)
            del q[0]

        if r_vals[:] == l_vals[:]:
            return True
        return False
```
