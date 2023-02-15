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
# n: 세로(엑스)
# 연결요소 개수 찾기, bfs로 푼다.
# 아 변수명 때문에 뭐가 잘 못 됐늦지 한참 헤맸다.....
# 바보야
from collections import deque
n,m=map(int, input().split())
graph=[]
for i in range(n):
    graph.append(list(map(int, input().split())))
    
dx=[0,0,1,-1]
dy=[1,-1,0,0]

def bfs(graph, x,y):
    queue= deque()
    queue.append((x,y))
    graph[x][y]=0
    count=1
    
    while queue:
        x,y=queue.popleft()
        
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            
            if nx<0 or ny<0 or nx>=n or ny>=m:
                continue
            if graph[nx][ny]==1:
                graph[nx][ny]=0
                queue.append((nx,ny))
                count += 1
    return count

result=[]
for i in range(n):
    for j in range(m):
        if graph[i][j]==1:
            result.append(bfs(graph, i,j))

if len(result) == 0:
    print(len(result))
    print(0)
else:
    print(len(result))
    print(max(result))
# -


