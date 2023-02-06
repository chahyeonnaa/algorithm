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
# 전류가 안쪽까지 침투하는지 판단하는 문제
# 상하좌우 이동 문제(땅모양 문제)
# bfs로 풀어야징
from collections import deque
def bfs(x,y):
    queue=deque()
    queue.append((x,y))
    
    while queue:
        x,y=queue.popleft()
        
        for i in range(4):
            nx= x+ dx[i]
            ny= y+ dy[i]
            
            if nx<0 or ny<0 or nx>=M or ny>=N:
                continue
            if graph[nx][ny]==0:
                graph[nx][ny]=2
                queue.append((nx,ny))
                
            
M,N=map(int, input().split())
graph=[]

# 상하좌우
dx=[-1,1,0,0]
dy=[0,0,-1,1]

for i in range(M):
    graph.append(list(map(int, input())))
    
# 바깥쪽 출발 제한 있음
for j in range(N):
    if graph[0][j]==0:
        bfs(0,j)

if graph[M-1].count(2):
    print("YES")
else:
    print("NO")
# -



