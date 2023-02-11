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
# bfs로 풀어야징
# 따로 방문 표시차 값을 바꿔주면 안되므로,, visited 배열이 필요하다.
# 0~최댓값까지 계속 새로 돌아야하므로 돌때마다 초기화해야함
# 결국은 연결요소의 개수세기다
from collections import deque
def bfs(x,y,visited, num):
    queue=deque()
    queue.append((x,y))

    while queue:
        x,y=queue.popleft()
        
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            
            if nx<0 or ny<0 or nx>=N or ny>=N:
                continue
                
            if graph[nx][ny]>num and visited[nx][ny]==0:
                visited[nx][ny]=1
                queue.append((nx,ny))
        
        
N=int(input())
graph=[]
result=0
max_num=0
for i in range(N):
    graph.append(list(map(int, input().split())))
    for j in range(N):
        if graph[i][j] > max_num:
            max_num=graph[i][j]
# 상하좌우            
dx=[-1,1,0,0]
dy=[0,0,-1,1]

for k in range(max_num):
    count=0
    visited=[[0]*N for _ in range(N)]
    
    for i in range(N):
        for j in range(N):
            # 안잠기는 영역을 세어야함
            if graph[i][j]>k and visited[i][j] ==0:
                bfs(i,j, visited, k)
                count+=1
    if result < count:
        result=count
                
print(result)
# -


