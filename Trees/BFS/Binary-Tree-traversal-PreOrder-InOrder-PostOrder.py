#!/usr/bin/env python3

# Definition for a binary tree node.
class TreeNode:
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

def preorderTraversal(self, root: TreeNode) :
    if root == None:
        return []
    else:
        return [root.val] + self.preorderTraversal(root.left) + self.preorderTraversal(root.right)

def inorderTraversal(self, root: TreeNode):
    if root:
        return self.inorderTraversal(root.left) + [root.val] + self.inorderTraversal(root.right)
    else:
        return []  

def postorderTraversal(self, root: TreeNode):
    if root:
        return self.postorderTraversal(root.left) + self.postorderTraversal(root.right) + [root.val]
    else:
        return []        