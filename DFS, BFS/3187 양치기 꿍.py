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
# 양이 늑대보다 많을 경우, 늑대가 잡아 먹힌다.
# 늑대가 양보다 많으면, 양이 잡아 먹힌다.
# 양과 늑대가 몇마리 살아남을 수 있을깍?
# R : 세로
from collections import deque
def bfs(x,y):
    v=0
    k=0
    queue=deque()
    queue.append((x,y))
    
    if graph[x][y]=='v':
        graph[x][y]="#"
        v+=1
    if graph[x][y]=='k':
        graph[x][y]="#"
        +=1
    
    while queue:
        x,y=queue.popleft()
        
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            
            if nx<0 or ny<0 or nx>=R or ny>=C or graph[nx][ny]=="#":
                continue
            if graph[nx][ny]==".":
                graph[nx][ny]="#"
                queue.append((nx,ny))
            elif graph[nx][ny]=="v":
                graph[nx][ny]="#"
                v +=1
                queue.append((nx,ny))
            elif graph[nx][ny]=="k":
                graph[nx][ny]="#"
                k +=1
                queue.append((nx,ny))
    return v,k


R,C=map(int, input().split())
graph=[]
for i in range(R):
    graph.append(list(input()))

dx=[-1,1,0,0]
dy=[0,0,-1,1]
v=0
k=0
for i in range(R):
    for j in range(C):
        if graph[i][j]!="#":
            A,B=bfs(i,j)
            if A<B:
                k += B
            else:
                v += A
print(k,v)
# -


