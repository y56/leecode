# 101. Symmetric Tree
## me, BFS for twice
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
## recursive 
```python=
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        def is_mirror(x, y):
            if not x and not y: 
                return True
            if not x or not y: # one is None, the other is not
                return False
            return (x.val == y.val) and is_mirror(x.left, y.right) and is_mirror(x.right, y.left)
        
        return is_mirror(root, root)
```
## iterative, one queue
```python=
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        q = [root, root]
        while q:
            x = q.pop(0)
            y = q.pop(0)
            if not x and not y: # both are None
                # you can't leave blank here
                pass # or use `continue` # or use `None`
            elif not x or not y: # one is None, one is not
                return False
            else:
                if x.val != y.val:
                    return False
                q.append(x.left)
                q.append(y.right)
                q.append(x.right)
                q.append(y.left)
        return True
```
## iterative, two queue
```python=
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        lq = [root]
        rq = [root]
        while lq and rq:
            l = lq.pop(0)
            r = rq.pop(0)
            if not l and not r: # both are None
                # you can't leave blank here
                pass # or use `continue`
            elif not l or not r: # one is None, one is not
                return False
            else:
                if l.val != r.val:
                    return False
                lq.append(l.left)
                lq.append(l.right)
                rq.append(r.right)
                rq.append(r.left)
        
        # we don't have to check this part
        # since there is only one tree, 
        # so the length is the same
        # if we are comparing two different trees,
        # we have to check this
        #
        # if lq or rq:
        #     return False
        
        return True
```
