#!/usr/bin/env python3
'''
102. Binary Tree Level Order Traversal
Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its level order traversal as:
[
  [3],
  [9,20],
  [15,7]
]
'''
from collections import deque
class Solution:
    def levelOrder(self, root):
        if not root: return [] #base case 
        res = []
        #queue to collect all the nodes
        #queue = deque([root]) 
        queue = deque()
        queue.append(root)

        while queue:
            level_vals = [] #hold the values at the current level.
            for _ in range(len(queue)): #evalute once before execution enter the loop
                node = queue.popleft()
                level_vals.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            #Add to result list afeter reading all node values in the level    
            res.append(level_vals)
        
        #whole queue is empty
        return res

#Driver code to build tree
class TreeNode():

    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

#Build binary tree [3,9,20,null,null,15,7]
root = TreeNode(3)
root.left  = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)

p = Solution()
print(p.levelOrder(root))        