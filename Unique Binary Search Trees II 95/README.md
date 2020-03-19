# 95. Unique Binary Search Trees II

## Catalan Numbers

## recursive

Using the idea of the math below

$$
C_0 = 1 \quad \text{and} \quad C_{n+1} = \sum_{i=0}^n C_i\,C_{n-i}\quad\text{for }n\ge 0
$$

```python=
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:
        
        
        def helper(start, end):
            
            if start>end:
                return [None] # null ptr as a terminating node
            
            roots=[]
            
            for i in range(start,end+1):
                
                left_nodes=helper(start, i-1)
                
                right_nodes=helper(i+1, end)
            
                for l in left_nodes:
                    for r in right_nodes:
                        roots.append(TreeNode(i))
                        roots[-1].left=l
                        roots[-1].right=r
            
            return roots
        
        if n==0:
            return []
        return helper(1,n)
```
## DP, re-using/pointing to previous/smaller trees


https://leetcode.wang/leetCode-95-Unique-Binary-Search-TreesII.html#%E8%A7%A3%E6%B3%95%E4%B8%89-%E5%8A%A8%E6%80%81%E8%A7%84%E5%88%92

```python=
def generateTrees(self, n: int) -> List[TreeNode]:

    if n==0:
        return []

    def clone_tree_and_give_offset(root_of_the_cloned, offset_to_add):
        if root_of_the_cloned == None:
            return None
        output_node = TreeNode(root_of_the_cloned.val + offset_to_add)
        output_node.left = clone_tree_and_give_offset(root_of_the_cloned.left, offset_to_add)
        output_node.right = clone_tree_and_give_offset(root_of_the_cloned.right, offset_to_add)
        return output_node

    dp = []
    for length in range(n+1): # need n+1 items
        dp.append([]) # not use [[]]*10 # they refer to the same empty list

    dp[0].append(None) # as the base case

    for length in range(1,n+1):
        for chosen_root_ind in range(1,length+1):
            len_of_left_tree = chosen_root_ind - 1
            len_of_right_tree = length - chosen_root_ind
            for root_of_left_tree in dp[len_of_left_tree]:
                for root_of_right_tree in dp[len_of_right_tree]:
                    root_of_all = TreeNode(chosen_root_ind)
                    root_of_all.left = root_of_left_tree
                    root_of_all.right = clone_tree_and_give_offset(root_of_right_tree, chosen_root_ind)
                    dp[length].append(root_of_all)
    return dp[n]
```

## DP/iterative
Using the idea of the math below
$$
C_0 = 1 \quad \text{and} \quad C_{n+1}=\frac{2(2n+1)}{n+2}C_n
$$

https://leetcode.wang/leetCode-95-Unique-Binary-Search-TreesII.html#%E8%A7%A3%E6%B3%95%E5%9B%9B-%E5%8A%A8%E6%80%81%E8%A7%84%E5%88%92-2

```python=
def generateTrees(self, n: int) -> List[TreeNode]:
    if n==0:
        return []

    def copy_a_tree(root):
        if root == None:
            return None
        new_root = TreeNode(root.val)
        new_root.left = copy_a_tree(root.left)
        new_root.right = copy_a_tree(root.right)
        return new_root

    pre = [None]

    for i in range(1,n+1):
        cur = []
        for root in pre:

            # insert as a new root # this part is certain to happen just once
            inserted_root = TreeNode(i)
            inserted_root.left = root
            cur.append(inserted_root)


            if root != None:
                # try to insert at other position, but not as a new root
                steps_to_take = 0 # remember how many steps we need to go right-down
                while True:
                    new_root = copy_a_tree(root)
                    focusing_node = new_root
                    for _ in range(steps_to_take):
                        focusing_node = focusing_node.right

                    original_right_child = focusing_node.right
                    inserted_node = TreeNode(i)
                    focusing_node.right = inserted_node
                    if original_right_child == None:
                        cur.append(new_root)
                        break
                    else:
                        inserted_node.left = original_right_child
                        cur.append(new_root)
                        steps_to_take += 1 # remember to go deeper at next time
        pre = cur

    return pre # OR, return pre # both work
```
