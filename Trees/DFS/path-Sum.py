#!/usr/bin/env python3
'''
112. Path Sum
Given a binary tree and a sum, determine if the tree has a root-to-leaf path such that adding up all the values along the path equals the given sum.

Note: A leaf is a node with no children.

Example:

Given the below binary tree and sum = 22,

      5
     / \\
    4   8
   /   / \\
  11  13  4
 /  \\      \\
7    2      1
return true, as there exist a root-to-leaf path 5->4->11->2 which sum is 22.
'''

def hasPathSum(root, sum):
    res = []
    dfs(root, sum, res)
    return any(res)


def dfs(root, target, res):
    if root:
        if not root.left  and not root.right:
            if root.val == target:
                res.append(True)
        if root.left:
            dfs(root.left, target-root.val, res)
        if root.right:
            dfs(root.right, target-root.val, res)

class TreeNode():

    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

#Build binary tree [3,9,20,null,null,15,7]
root = TreeNode(5)
root.left  = TreeNode(4)
root.right = TreeNode(8)
root.left.left = TreeNode(11)
root.left.left.left = TreeNode(7)
root.left.left.right = TreeNode(2)

root.right.left = TreeNode(13)
root.right.right = TreeNode(4)
root.right.right.right = TreeNode(1)

print(hasPathSum(root, 22))
