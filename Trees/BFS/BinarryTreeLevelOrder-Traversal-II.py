#!/usr/bin/env python3

'''
107. Binary Tree Level Order Traversal II
Given a binary tree, return the bottom-up level order traversal of its nodes' values. (ie, from left to right, level by level from leaf to root).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its bottom-up level order traversal as:
[
  [15,7],
  [9,20],
  [3]
]

'''

'''
Simple solution is just reverse the result from Level Order I problem
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
        res.reverse()
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