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
# 연결요소의 개수를 찾는데, 거기서 더 나아가서 각 연결요소의 개수 구하기!
# bfs로 풀어야징
# 이동판 문제, 방문했으면 방문표시 하는거 개중요 ㅠㅠ 한참을 헤맸다
from collections import deque
def bfs(x,y):
    queue=deque()
    queue.append((x,y))
    graph[x][y]=0
    count=1
    
    while queue:
        x,y=queue.popleft()
        graph[x][y]=0
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            
            if nx<0 or ny<0 or nx>=N or ny>=N:
                continue
            if graph[nx][ny]==1:
                graph[nx][ny]=0
                queue.append((nx, ny))
                count+=1
    return count
                
                
N=int(input())
graph=[]
A=[]
s=0
for _ in range(N):
    graph.append(list(map(int, input())))

# 상하좌우
dx=[-1,1,0,0]
dy=[0,0,-1,1]
result=[]
cnt=0
for i in range(N):
    for j in range(N):
        if graph[i][j]==1:
            result.append(bfs(i,j))
result.sort()
print(len(result))
for i in range(len(result)):
    print(result[i])
# -


