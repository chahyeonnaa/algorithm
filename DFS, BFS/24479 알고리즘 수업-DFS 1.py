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
# 런타임에러
def dfs(R,visited,graph):
    visited[R]=True
    print(R)

    for i in graph[R]:
        if not visited[i]:
            dfs(i,visited,graph)
            
N,M,R=map(int, input().split())
visited=[False]*(N+1)
graph=[[]*N for _ in range(N+1)]

for _ in range(M):
    A,B=map(int, input().split())
    graph[A].append(B)
    graph[B].append(A)

for i in range(M):
    graph[i].sort()
    
dfs(R,visited,graph)

for i in range(1,N+1):
    if visited[i]==False:
        print(0)
# -


