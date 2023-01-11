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
# dfs 점점 이해 되는중. but.. 아직 부족하다
# 처참히 시간초과........
import sys
sys.setrecursionlimit(10000)
N,M=map(int, input().split())
graph=[[] for _ in range(N+1)]
visited=[False]*(N+1)
result=0
def dfs(graph, v, visited):
    visited[v]=True
    
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)
            
for i in range(M):
    A,B=map(int, input().split())
    graph[A].append(B)
    graph[B].append(A)

for i in range(1, N+1):
    if visited[i]==False:
        dfs(graph, i, visited)
        result +=1
print(result)
    
# -


