#!/usr/bin/env python3

'''
199. Binary Tree Right Side View
Given a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.

Example:

Input: [1,2,3,null,5,null,4]
Output: [1, 3, 4]
Explanation:

    1            <---
       
    2     3         <---
         
    5     4       <---

'''

from collections import deque
class Solution:
    def BinaryTreeRightSideView(self, root):
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
            res.append(level_vals[-1])
        
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
print(p.BinaryTreeRightSideView(root))        