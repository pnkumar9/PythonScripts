#!/usr/bin/env python3
'''
543. Diameter of Binary Tree
Given a binary tree, you need to compute the length of the diameter of the tree. The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.

Example:
Given a binary tree
          1
         / \\
        2   3
       / \\     
      4   5    
Return 3, which is the length of the path [4,2,1,3] or [5,2,1,3].

Note: The length of path between two nodes is represented by the number of edges between them.
'''

class Solution:
    def diameterOfBinaryTree(self, root):
        self.diameter = 0
        self.dfs(root)
        return self.diameter
    
    def dfs(self, node):
        # base case:
        if node == None:
            return 0
		# recursive cases
        left_height = self.dfs(node.left)
        right_height = self.dfs(node.right)
        self.diameter = max(self.diameter,left_height + right_height )
        return max(left_height,right_height) + 1       

'''
          1
         / \\
        2   3
       / \\     
      4   5   
'''
class TreeNode():

    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

root = TreeNode(1)
root.left  = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

p = Solution()
print(p.diameterOfBinaryTree(root))
