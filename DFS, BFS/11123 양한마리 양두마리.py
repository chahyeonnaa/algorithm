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
# H(가로) W(세로)
# bfs로 풀어야징
# 성공 ~~~ bfs 점점 이해하는중 !
from collections import deque
def bfs(x,y):
    queue=deque()
    queue.append((x,y))
    
    while queue:
        x,y=queue.popleft()
        
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            
            if nx<0 or ny<0 or nx>=H or ny>=W:
                continue
            if graph[nx][ny]=="#":
                queue.append((nx,ny))
                graph[nx][ny]="."
                             
T=int(input())
for i in range(T):
    graph=[]
    # 상하좌우
    dx=[-1,1,0,0]
    dy=[0,0,-1,1]
    count=0
    H,W=map(int, input().split())
    for _ in range(H):
        graph.append(list(map(str, input())))
        
    for i in range(H):
        for j in range(W):
            if graph[i][j]=="#":
                bfs(i,j)
                count+=1
    print(count)
# -


