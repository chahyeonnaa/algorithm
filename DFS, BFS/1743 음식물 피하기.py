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
# 연결 요소 개수 중에 제일 큰 것 구하기 
# 판을 먼저 만들어야함
# bfs로 풀어야징 / N: 세로
# 성공!
from collections import deque
def bfs(x,y):
    count=1
    queue=deque()
    queue.append((x,y))
    graph[x][y]=0
    
    while queue:
        x,y=queue.popleft()
        
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            
            if nx<0 or ny<0 or nx>=N or ny>=M:
                continue
            if graph[nx][ny]==1:
                graph[nx][ny]=0
                queue.append((nx,ny))
                count+=1
    return count
        
N,M,K=map(int, input().split())
graph=[[0]*M for _ in range(N)]
dx=[-1,1,0,0]
dy=[0,0,-1,1]
result=[]
for _ in range(K):
    A,B=map(int, input().split())
    graph[A-1][B-1]=1
    
for i in range(N):
    for j in range(M):
        if graph[i][j]==1:
            result.append(bfs(i,j))
print(max(result))
# -


