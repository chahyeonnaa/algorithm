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
# 나는 같은 촌수끼리를 다 다르게 카운팅해서 20퍼에서 틀림
# 연결된 노드를 세는게 아니라, 한단계는 다 같은 촌수로 취급해야함!!!
# 하나의 간선으로 연결된 노드들은 같은 촌수로 취급해야함 !!!!
# 어렵다!
# 문제풀때 집중 안하면 오래 걸리고 놓치는 부분 생긴다... 딴 짓 금지..
from collections import deque

def bfs(start):
    queue=deque([start])
    
    while queue:
        v=queue.popleft()
        
        for i in graph[v]:
            if visited[i]==-1:
                queue.append(i)
                visited[i]=visited[v]+1
                
N=int(input())
visited=[-1]*(N+1)
A,B=map(int, input().split())
M=int(input())
graph=[[]*N for _ in range(N+1)]

for i in range(M):
    x,y=map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)
    
visited[A]=0
bfs(A)
print(visited[B])
# -


