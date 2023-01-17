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
def bfs(graph, start, visited):
    queue=deque([start])
    visited[start]=True
    
    while queue:
        v=queue.popleft()
        #print(v, end=" ")
        for i in graph[v]:
            if not visited[i]:
                visited[i]=True
                queue.append(i)

N,M=map(int, input().split())
graph=[[]*N for _ in range(N+1)]
visited=[False]*(N+1)
result=0
for i in range(M):
    A,B=map(int, input().split())
    graph[A].append(B)
    graph[B].append(A)
    
#print(graph)
for i in range(1, N+1):
    if visited[i]==False:
        bfs(graph, i, visited)
        result+=1

print(result)

# -


