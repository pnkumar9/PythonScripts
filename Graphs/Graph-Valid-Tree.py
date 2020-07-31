#!/usr/bin/env python3
'''
261. Graph Valid Tree
Given n nodes labeled from 0 to n-1 and a list of undirected edges (each edge is a pair of nodes),
 write a function to check whether these edges make up a valid tree.

Example 1:

Input: n = 5, and edges = [[0,1], [0,2], [0,3], [1,4]]
Output: true
Example 2:

Input: n = 5, and edges = [[0,1], [1,2], [2,3], [1,3], [1,4]]
Output: false
Note: you can assume that no duplicate edges will appear in edges. Since all edges are undirected, [0,1] is the same as [1,0] and thus will not appear together in edges.
'''

'''
A Tree is a connected graph with no cycles.
It shouldn't contain more than 1 component.

'''
from collections import defaultdict

def graph_valid_tree(n, edges):

    #build adjList
    adjList = defaultdict(list)
    no_of_components = 0

    for src, dst in edges:
        adjList[src].append(dst)
        adjList[dst].append(src)

    #print(f"adjList: {adjList}")
    visited = [-1] * n
    parent = [-1] * n

    #call bfs
    for node in range(n):
        if visited[node] == -1:
            no_of_components += 1
            if no_of_components > 1:
                return False # It's not connected graph so it's not tree
            cycle_exist = bfs(node, adjList, visited, parent)
            if cycle_exist:
                return False
            


    return True

from collections import deque 
#find cycle in graph
def bfs(node, adjList, visited, parent):
    q = deque()
    q.append(node)
    visited[node] = 1

    #print(f"parent at the begining: {parent}")
    #print(f"adjList at the begining: {adjList}")

    while q:
        vertex = q.popleft()

        for neighbor in adjList[vertex]:
            if visited[neighbor] == -1:
                visited[neighbor] = 1
                parent[neighbor] = vertex
                #print(f"updating parent for child {neighbor} Now Parent is {parent}")
                q.append(neighbor)
            else:
                if neighbor != parent[vertex]: #cross edge
                    #print(f"cycle found neighbor: {neighbor} of {vertex} parent: {parent[vertex]} parent array: {parent}")
                    return True             


    return False                    

print(graph_valid_tree(5,  [[0,1], [0,2], [0,3], [1,4]] ))    
print(graph_valid_tree(5,  [[0,1], [1,2], [2,3], [1,3], [1,4]] ))

from collections import deque 
import collections
def validTree(n, edges):        
    if len(edges) != n - 1:  # Check number of edges.
        return False

    # init node's neighbors in dict
    neighbors = collections.defaultdict(list)
    for u, v in edges:
        neighbors[u].append(v)
        neighbors[v].append(u)

    # BFS to check whether the graph is valid tree.
    visited = {}
    q = collections.deque([0])
    while q:
        curr = q.popleft()
        visited[curr] = True
        for node in neighbors[curr]:
            if node not in visited:
                visited[node] = True
                q.append(node)

    return len(visited)==n

print(validTree(5,  [[0,1], [0,2], [0,3], [1,4]] ))    
print(validTree(5,  [[0,1], [1,2], [2,3], [1,3], [1,4]] ))    