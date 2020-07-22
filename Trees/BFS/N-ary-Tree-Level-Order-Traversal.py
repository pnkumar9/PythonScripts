#!/usr/bin/env python3
'''
429. N-ary Tree Level Order Traversal
Given an n-ary tree, return the level order traversal of its nodes' values.

Nary-Tree input serialization is represented in their level order traversal, each group of children is separated by the null value (See examples).
Input: root = [1,null,3,2,4,null,5,6]
Output: [[1],[3,2,4],[5,6]]

Input: root = [1,null,2,3,4,5,null,null,6,7,null,8,null,9,10,null,null,11,null,12,null,13,null,null,14]
Output: [[1],[2,3,4,5],[6,7,8,9,10],[11,12,13],[14]]
'''

from collections import deque
class Solution:
    def levelOrder_N_ary(self, root):
        if not root: 
            return [] #base case 
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
                for child in node.children:
                    queue.append(child)

            #Add to result list afeter reading all node values in the level    
            res.append(level_vals)
        
        #whole queue is empty
        return res

    def levelOrder(self, root):
        stack,level,result = deque(),[],[]
        if not root:
            return [] 
        stack.append(root)
        while stack:
            for i in range(len(stack)):
                popped = stack.popleft()
                level.append(popped.val)
                for i in (popped.children):
                    stack.append(i)
            result.append(level)
            level = []
        return result        

#Driver code to build N-ary tree
class TreeNode():

    def __init__(self, val=None, children=None):
        self.val = val
        self.children = []

#Build binary tree [3,9,20,null,null,15,7]
root = TreeNode(1)
root.children.append(TreeNode(3))
root.children.append(TreeNode(2))
root.children.append(TreeNode(4))

root.children[0].children.append(TreeNode(5))
root.children[0].children.append(TreeNode(6))

p = Solution()
print(p.levelOrder_N_ary(root))   
print(p.levelOrder(root))  