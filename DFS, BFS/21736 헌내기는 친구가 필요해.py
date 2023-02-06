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
# 상하좌우 이동가능, 도연이가 만날 수 있는 사람의 수 출력
# 0 빈공간, X 벽, I 도연이, P 사람
# 0이면 이동가능, P를 만나면 카운트
# bfs로 풀어야징
from collections import deque
def bfs(x,y):
    global count
    queue=deque()
    queue.append((x,y))
    
    while queue:
        x,y=queue.popleft()
        
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            
            if nx<0 or ny<0 or nx>=N or ny>=M:
                continue    
            # 아 여기서 걸린다. X로 둘러싸인 P..어떻게 제한해주지? 
            # 어떻게 제한을 걸지..?
            if graph[nx][ny]=="X":
                continue
            if graph[nx][ny]=="P":
                count+=1
            if graph[nx][ny]=="0":
                graph[nx][ny]=-1
                queue.append((nx,ny))
                
            
N,M=map(int, input().split())
graph=[]
count=0
# 상하좌우
dx=[-1,1,0,0]
dy=[0,0,-1,1]

for _ in range(N):
    graph.append(list(map(str, input())))
        
# 도연이 위치에서 출발해야함
for i in range(N):
    for j in range(M):
        if graph[i][j]=="I":
            bfs(i,j)
        
        
if count==0:
    print("TT")
else:
    print(count)
# -


