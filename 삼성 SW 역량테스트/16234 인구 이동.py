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
# 국경열기까지는 OK -> 열려있는 위치값들을 한꺼번에 리턴해주는 것이 핵심
# 처음에 국경열고, 다 똑같은 값들로 바꿔주기 -> 또 바꿀게 있는지 계속 확인해야함
# L과 R에 걸리는지는 bfs 함수 안에서 확인함 -> 무한반복문, flag 사용
# 반복문 안에서 len(country)에 안걸리면(bfs함수 안에서 조건에 안걸리면 길이가 1임) 무한반복문 탈출
# 전체 프로세스 : 무한반복 -> bfs로 조건 확인...

from collections import deque
def bfs(x,y):
    queue=deque()
    temp=[]
    queue.append([x,y])
    temp.append([x,y])
    while queue:
        x,y=queue.popleft()
        for i in range(4):
            rx=x+dx[i]
            ry=y+dy[i]
            
            if rx>=0 and rx<N and ry>=0 and ry<N and visited[rx][ry]==0:
                if L<=abs(graph[rx][ry]-graph[x][y])<=R:
                    queue.append([rx,ry])
                    visited[x][y]=1
                    visited[rx][ry]=1
                    temp.append([rx,ry])
    return temp      
        
N,L,R=map(int, input().split())
graph=[]
# 상,하,좌,우 
dx=[-1,1,0,0]
dy=[0,0,-1,1]

result=0
for i in range(N):
    graph.append(list(map(int, input().split())))

while True:
    visited=[[0]*N for _ in range(N)]
    flag=0
    for i in range(N):
        for j in range(N):
            if visited[i][j]==0:
                country=bfs(i,j)
            
                if len(country)>1:
                    flag=1
                    A=0
                    for x,y in country:
                        A += graph[x][y]
                    number=A//len(country)
                    for x,y in country:
                        graph[x][y]=number
    if flag==0:
        break

    result+=1
                
print(result)
# -


