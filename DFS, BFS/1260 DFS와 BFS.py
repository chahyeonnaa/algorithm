# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py:light
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.14.4
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

# +
from collections import deque
def dfs(graph, v, visited):
    visited[v]=True
    print(v, end=" ")
    
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)
    
def bfs(graph, start, visited):
    queue=deque([start])
    visited[start]=True
    print(start, end=" ")
    while queue:
        v=queue.popleft()
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i]=True
                print(i, end=" ")
    
N,M,V=map(int, input().split())
graph=[[]*N for _ in range(N+1)]
visited=[False]*(N+1)
for i in range(M):
    A,B=map(int, input().split())
    graph[A].append(B)
    graph[B].append(A)
    graph[A].sort()
    graph[B].sort()

dfs(graph, V, visited)
print()
visited=[False]*(N+1)
bfs(graph, V, visited)

# -


