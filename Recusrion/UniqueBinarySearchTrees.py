#!/usr/bin/env python3
'''
96. Unique Binary Search Trees
Given n, how many structurally unique BST's (binary search trees) that store values 1 ... n?

Example:

Input: 3
Output: 5
Explanation:
Given n = 3, there are a total of 5 unique BST's:

   1         3     3      2      1
 
     3     2     1      1   3      2
 
   2     1         2                 3


Constraints:

1 <= n <= 19
'''


'''
We are supposed to find out the number of unique binary trees from the sequence 1....n
This means the number of nodes is n

Lets us start by saying that we will have 0 left nodes. That means right nodes will be n - 1. We are subtracting 1 from n because out of the n nodes there will be a root too. Hence, n - 1 right nodes.
Similarly if we have 1 left node that means right nodes will be n - 1 - 1. One 1 is being subracted from n because of the root node and one 1 is being subtracted because of 1 left node.
We will have to do this for 0 left nodes to n -1 left nodes. Read ( range(0,n) in python)
Now since we know the number of nodes in left and right subtrees, we can recursively call the function on these.
Our base case if n == 0, which is 1 because if n = 0, only null/empty tree would be present.
'''

'''
video explanation: https://www.youtube.com/watch?v=YDf982Lb84o

'''
class Solution:
    def numTrees(self, n: int) -> int:
        if n == 0:
            return 1
            
        numSubtrees = 0
        for leftSubtreeNodeCount in range(n):
            rightSubtreeNodeCount = n - 1 - leftSubtreeNodeCount
            leftSubtrees = self.numTrees(leftSubtreeNodeCount)
            rightSubtrees = self.numTrees(rightSubtreeNodeCount)
            numSubtrees += leftSubtrees * rightSubtrees
        return numSubtrees

p = Solution()

print(p.numTrees(1))
print(p.numTrees(2))
print(p.numTrees(3))
print(p.numTrees(4))
print(p.numTrees(5))

#With memoization to prevent calculating for same n multiple times. Similar to Fibonacci
class Solution2:
    def numTrees(self, n: int, cache={}) -> int:
        if n == 0:
            return 1
        if n in cache:
            return cache[n]
        numSubtrees = 0
        for leftSubtreeNodeCount in range(n):
            rightSubtreeNodeCount = n - 1 - leftSubtreeNodeCount
            leftSubtrees = self.numTrees(leftSubtreeNodeCount, cache)
            rightSubtrees = self.numTrees(rightSubtreeNodeCount, cache)
            #This is Cartesian product
            numSubtrees += leftSubtrees * rightSubtrees
        cache[n] = numSubtrees
        return numSubtrees