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
# . 비어있다 / # 울타리 / o 양 / v 늑대
# 같은 영역(연결 요소)안에서 양이 늑대보다 많으면 이긴다. 적으면 잡아먹힘
# -> 양이 늑대보다 많아야만 양이 살아남고, 아니면 늑대가 산다.
# 연결요소 안에서 양과 늑대의 수를 세어서 판단!
# 아침이 왔을 때 살아남은 양과 늑대의 수는?
# 핵심은 연결요소 안에서 v와 o의 개수를 세는 것....
# R : 세로 
# 도전중. 처음부터 visited 배열 안쓰고 풀었는데 왜 안풀리는지 모르ㅔㅆ다.
from collections import deque
def bfs(x,y):
    v=0
    o=0
    
    queue=deque()
    queue.append((x,y))
    
    if graph[x][y]=='v':
        graph[x][y]="#"
        v+=1
    if graph[x][y]=='o':
        graph[x][y]="#"
        o+=1
    
    while queue:
        x,y=queue.popleft()
        
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            
            if nx<0 or ny<0 or nx>=R or ny>=C:
                continue
            if 0 <= nx < R and 0 <= ny < C:
                if graph[nx][ny]=="v":
                    graph[nx][ny]="#"
                    v+=1
                if graph[nx][ny]=="o":
                    graph[nx][ny]="#"
                    o+=1
                queue.append((nx,ny))
                
    return v,o


R,C=map(int, input().split())
graph=[]
dx=[-1,1,0,0]
dy=[0,0,-1,1]
result_v=0
result_o=0

for i in range(R):
    graph.append(list(input()))

for i in range(R):
    for j in range(C):
        if graph[i][j]!="#":
            A,B= bfs(i,j)
            # 늑대가 더 많으면, 늑대는 다 생존
            if A>=B:
                result_v += A
            else:
                result_o += B
print(result_o, result_v)
# -


