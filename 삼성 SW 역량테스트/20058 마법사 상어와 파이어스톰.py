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
N,Q=map(int, input().split())
graph=[]
for i in range(2**N):
    graph.append(list(map(int, input().split())))
L=list(map(int, input().split()))

# 필요한 기본 정보
dx=[-1,1,0,0]
dy=[0,0,-1,1]

# 배열 회전 함수
def rotate(graph, l):
    new_graph=[[0]*(2**N) for _ in range(2**N)]
    
    for i in range(0,2**N, 2**l):
        for j in range(0,2**N,2**l):
            for k in range(2**l):
                for m in range(2**l):
                    new_graph[i+k][j+m]=graph[i + (2**l - 1 - m)][j+k]

    return new_graph

# 줄어들어야 하는 얼음 체크
def melt(graph):
    new_graph=[[0]*(2**N) for _ in range(2**N)]
    
    for i in range(2**N):
        for j in range(2**N):
            count=0
            for k in range(4):
                nx=i+dx[k]
                ny=j+dy[k]
                
                if 0<=nx<2**N and 0<=ny<2**N:
                    if graph[nx][ny]>0:
                        count+=1
            if count<3:
                new_graph[i][j]=graph[i][j]-1
            else:
                new_graph[i][j]=graph[i][j]
    return new_graph
                
            
# 연산 수행
for i in range(Q):
    ice_graph=rotate(graph, L[i])
    ice_graph=melt(ice_graph)

# 필요한 결과 계산 - 최대 연결요소 개수 찾기
# 0이 아니면 얼음이 있는 것!
visited=[[0]*(2**N) for _ in range(2**N)]
sum_ice=0
max_size=0
for i in range(2**N):
    for j in range(2**N):
        if visited[i][j]==0 and ice_graph[i][j]>0:
            check = [[i, j]]
            sum_ice += ice_graph[i][j]
            visited[i][j] = True
            count = 1
            #그 칸을 기준으로 얼음 덩어리 찾기
            while check:
                x, y = check.pop(0)

                #4가지 방향에서
                for dir in range(4):
                    nx = x + dx[dir]
                    ny = y + dy[dir]

                    #범위 이내이고, 얼음이 있으며 방문하지 않은 칸일때
                    if 0 <= nx < 2**N and 0 <= ny < 2**N:
                        if ice_graph[nx][ny] > 0 and visited[nx][ny] == False:
                            #얼음의 크기를 세고 방문처리후 현재 얼음 덩어리 크기 + 1
                            sum_ice += ice_graph[nx][ny]
                            check.append([nx, ny])
                            visited[nx][ny] = True
                            count += 1

            max_size = max(max_size, count)
print(sum_ice)
print(max_size)
