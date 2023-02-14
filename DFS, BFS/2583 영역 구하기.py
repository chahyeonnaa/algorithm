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
# M : 세로, 엑스
# bfs로 풀어야징
# ㅇ와아아ㅏ아아 성공성공성공 ~!!!
from collections import deque
def bfs(x,y):
    cnt=0
    queue=deque()
    queue.append((x,y))
    cnt +=1
    
    while queue:
        x,y=queue.popleft()
        graph[x][y]=-1
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            
            if nx<0 or ny<0 or nx>=M or ny>=N:
                continue
            if graph[nx][ny]==0:
                graph[nx][ny]=-1
                queue.append((nx,ny))
                cnt+=1
    return cnt
                
M,N,K=map(int, input().split())
graph=[[0]*N for _ in range(M)]
for _ in range(K):
    a,b,c,d=map(int, input().split())
    
    for i in range(a,c):
        for j in range(b,d):
            if graph[j][i]==0:
                graph[j][i]=1

dx=[-1,1,0,0]
dy=[0,0,-1,1]
result=[]
for i in range(M):
    for j in range(N):
        if graph[i][j]==0:
            result.append(bfs(i,j))
            
print(len(result))
result.sort()
print(*result)
            

# -


