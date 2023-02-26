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
# 연결요소의 개수 찾기
# 대각선도 하나로 인정
# M 세로
# 성공!
from collections import deque
def bfs(x,y):
    queue=deque()
    queue.append((x,y))
    graph[x][y]=0
    
    while queue:
        x,y=queue.popleft()
        
        for i in range(8):
            nx=x+dx[i]
            ny=y+dy[i]
            
            if nx<0 or ny<0 or nx>=M or ny>=N:
                continue
            if graph[nx][ny]==1:
                graph[nx][ny]=0
                queue.append((nx, ny))
                
M,N=map(int, input().split())
graph=[]
for _ in range(M):
    graph.append(list(map(int, input().split())))

# 상,하,좌,우, 대각선 4개
dx=[-1,1,0,0,-1,-1,1,1]
dy=[0,0,-1,1,1,-1,-1,1]
count=0
for i in range(M):
    for j in range(N):
        if graph[i][j]==1:
            bfs(i,j)
            count +=1
print(count)
