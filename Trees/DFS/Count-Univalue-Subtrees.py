#!/usr/bin/env python3
'''
Given a binary tree, count the number of uni-value subtrees.

A Uni-value subtree means all nodes of the subtree have the same value.

Example :

Input:  root = [5,1,5,5,5,null,5]

              5
             / \\
            1   5
           / \\   \\
          5   5   5

Output: 4
'''


class TreeNode():

    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

#Build binary tree [5,1,5,5,5,null,5]
root = TreeNode(5)
root.left  = TreeNode(1)
root.right = TreeNode(5)
root.left.left = TreeNode(5)
root.left.right = TreeNode(5)
root.right.right = TreeNode(5)


class Solution:
    
    def __init__(self):
        self.count = 0
    
    def isUni(self, node):
        if node.left == None and node.right == None:
            self.count += 1
            return True
        res = True
        if node.left:
            res = self.isUni(node.left) and node.val == node.left.val and res
        if node.right:
            res = self.isUni(node.right) and node.val == node.right.val and res
        if res:
            self.count += 1
        return res
    
    def countUnivalSubtrees(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root != None:
            self.isUni(root)
        return self.count

p = Solution()
print(p.countUnivalSubtrees(root))