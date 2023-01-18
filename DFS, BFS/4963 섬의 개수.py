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
# 성공!
from collections import deque
def bfs(x,y):
    queue=deque()
    queue.append((x,y))
    
    while queue:
        x,y=queue.popleft()
        for i in range(8):
            nx=x+dx[i]
            ny=y+dy[i]
            
            if nx<0 or nx>=H or ny<0 or ny>=W:
                continue
            if graph[nx][ny]==0:
                continue
            if graph[nx][ny]==1:
                graph[nx][ny]=0
                queue.append((nx,ny))


while True:
    result=0
    W,H=map(int, input().split())
    graph=[[]*W for _ in range(H)]
    dx=[0,0,-1,1,-1,-1,1,1]
    dy=[1,-1,0,0,1,-1,-1,1]
    
    
    if W==0 and H==0:
        break
    for i in range(H):
        S=list(map(int, input().split()))
        graph[i]=S
        
    for i in range(H):
        for j in range(W):
            if graph[i][j]==1:
                bfs(i,j)
                result+=1
    print(result)
    
# -


