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
# 2606 바이러스 - 배열 범위 고려하기, 런타임 에러 주의
N=int(input())
S=int(input())
graph=[[]*N for _ in range(N+1)]
visited=[False]*(N+1)
count=0

def dfs(graph, v, visited):
    global count
    visited[v]=True
    count+=1
    
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)
    
for i in range(S):
    A,B=map(int, input().split())
    graph[A].append(B)
    graph[B].append(A)

dfs(graph, 1, visited)
print(count-1)
