#!/usr/bin/env python3
'''
323. Number of Connected Components in an Undirected Graph
Given n nodes labeled from 0 to n - 1 and a list of undirected edges (each edge is a pair of nodes), write a function to find the number of connected components in an undirected graph.

Example 1:

Input: n = 5 and edges = [[0, 1], [1, 2], [3, 4]]

     0          3
     |          |
     1 --- 2    4 

Output: 2
Example 2:

Input: n = 5 and edges = [[0, 1], [1, 2], [2, 3], [3, 4]]

     0           4
     |           |
     1 --- 2 --- 3

Output:  1
'''
from collections import defaultdict

def connected_components_bfs(n, edges):

    #build adjList
    adjList = defaultdict(list)
    no_of_components = 0

    for src, dst in edges:
        adjList[src].append(dst)
        adjList[dst].append(src)

    print(f"adjList: {adjList}")
    visited = [-1] * n

    #call bfs
    for node in range(n):
        if visited[node] == -1:
            bfs(node, adjList, visited)
            no_of_components += 1


    return no_of_components

from collections import deque 

def bfs(node, adjList, visited):
    q = deque()
    q.append(node)
    visited[node] = 1

    while q:
        vertex = q.popleft()

        for neighbor in adjList[vertex]:
            if visited[neighbor] == -1:
                visited[neighbor] = 1
                q.append(neighbor)



print(connected_components_bfs(5, [[0, 1], [1, 2], [3, 4]]))
print(connected_components_bfs(5, [[0, 1], [1, 2], [2, 3], [3, 4]]))


def connected_components_dfs(n, edges):
    #build adjList
    adjList = defaultdict(list)
    no_of_components = 0

    for src, dst in edges:
        adjList[src].append(dst)
        adjList[dst].append(src)

    print(f"adjList: {adjList}")
    visited = [-1] * n

    #call dfs
    for node in range(n):
        if visited[node] == -1:
            dfs(node, adjList, visited)
            no_of_components += 1


    return no_of_components

def dfs(node, adjList, visited):
    visited.append(node)
    for neighbor in adjList[node]:
        if visited[neighbor] == -1:
            dfs(node, adjList, visited)        

#print(connected_components_dfs(5, [[0, 1], [1, 2], [3, 4]]))
#print(connected_components_dfs(5, [[0, 1], [1, 2], [2, 3], [3, 4]]))
import collections
def countComponents(n, edges):
    graph = collections.defaultdict(list)
    for x, y in edges:
        graph[x].append(y)
        graph[y].append(x)
    
    def dfs(node, seen):
        seen.add(node)
        for neighbor in graph[node]:
            if neighbor not in seen:
                dfs(neighbor, seen)
    count = 0
    seen = set()
    for node in range(n):
        if node not in seen:
            dfs(node, seen)
            count += 1
    return count

print(countComponents(5, [[0, 1], [1, 2], [3, 4]]))
print(countComponents(5, [[0, 1], [1, 2], [2, 3], [3, 4]]))    