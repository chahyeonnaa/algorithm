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
import sys
input=sys.stdin.readline

def dfs(R):
    global count
    visited[R]=count
    
    for i in graph[R]:
        if visited[i]==0:
            count +=1
            dfs(i)

N,M,R=map(int, input().split())
graph=[[]*N for _ in range(N+1)]
visited=[0]*(N+1)
count=1
for _ in range(M):
    A,B=map(int, input().split())
    graph[A].append(B)
    graph[B].append(A)
    
    
for i in range(1, N+1):
    graph[i].sort(reverse=True)
    
dfs(R)

for i in range(1, N+1):
    print(visited[i])
