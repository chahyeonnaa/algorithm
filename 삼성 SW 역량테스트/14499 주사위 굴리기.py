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
# 와 처음으로...처음부터 끝까지 내 힘으로 해결 !!!!!!!
from collections import deque
N,M,x,y,K=map(int, input().split())
graph=[]

def rot(number):
    if number==1:
        leftright.rotate(-1)
        updown[1]=leftright[1]
        updown[3]=leftright[3]
    elif number==3:
        updown.rotate(1)
        leftright[1]=updown[1]
        leftright[3]=updown[3]
    elif number==2:
        updown.rotate(-1)
        leftright[1]=updown[1]
        leftright[3]=updown[3]
    elif number==0:
        leftright.rotate(1)
        updown[1]=leftright[1]
        updown[3]=leftright[3]
        
for i in range(N):
    S=list(map(int, input().split()))
    graph.append(S)
remove=list(map(int, input().split())) 

# 동0 서1 북2 남3
dx=[0,0,-1,1]
dy=[1,-1,0,0]

# 1번째 인덱스를 바닥으로 고정
# 두 큐에서 1,3은 공통적으로 값을 바꿔줘야함
updown=deque([0,0,0,0])
leftright=deque([0,0,0,0])
result=[]

for i in range(K):
    nx=x+dx[remove[i]-1]
    ny=y+dy[remove[i]-1]
    
    if nx<0 or ny<0 or nx>=N or ny>=M:
        continue
        
    if graph[nx][ny]==0:
        rot(remove[i]-1)    
        graph[nx][ny]=updown[1]
    elif graph[nx][ny]!=0:
        rot(remove[i]-1)
        updown[1]=graph[nx][ny]
        leftright[1]=graph[nx][ny]
        graph[nx][ny]=0
    x=nx
    y=ny
    result.append(updown[3])
    
print(*result, sep="\n")
        
# -


