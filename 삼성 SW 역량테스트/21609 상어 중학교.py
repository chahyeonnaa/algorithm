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
# 검은색(-1), 무지개색(0), 일반 블록(M이하의 자연수로 표현)
# 인접칸 정의 : 상하좌우

# 블록 그룹 정의 : 일반 블록이 적어도 1개, 색은 모두 같아야함
# 검은 블록(-1)은 포함하면 안돼! 

# 순서
# 가장 크기가 큰 블록 그룹 찾기 -> 같으면 무지개, 행, 열 큰순
# 찾은 블록 그룹 값을 다 -2로 바꿔주기, 개수세어서 제곱만큼 점수 획득
# 중력 작용 : -1, -2가 아닌 블록들이, 인덱스 범위 벗어나거나 다른 블록들을 만날 때까지 이동. 행이 커지는 순서로
# 반시계 90도 == 270도 회전
# 다시 중력 작용
# 블록 그룹이 존재하는 동안 위의 과정이 계속 반복!

# 1. 크기가 가장 큰 블록 그룹 찾기 = 연결요소 개수 찾기?
# 2. 중력 작용
# 전체를 돈다. 밑에 칸이 비어있으면 내려간다. 안비어있거나 끝이 될때 까지
# 3. 회전

# 몇개가 안나오는데 왜그런지를 모르겠다 ㅠㅠㅠㅠ
from collections import deque 
# 중력 작용
def earth(graph):
    for i in range(N):
        for j in range(N):
            # 검은색이거나, 비어있거나
            if graph[i][j]==-1 or graph[i][j]==-2:
                continue
            # 경계에 도달하거나, 다른 블록을 만나면(빈칸이 아니면)
            if i+1>=N or graph[i+1][j]!=-2:
                continue
            # 어차피 전체 칸을 검사하니까 무한반복문 안걸어도 될듯
            graph[i+1][j]=graph[i][j]
            # 이동 했으면 빈칸으로 만들어주기
            graph[i][j]=-2
            
def rotate():
    new_graph=[[0]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            new_graph[N-1-j][i]=graph[i][j]
    # 이렇게 바로 바꿔줘도 되는건지 몰겠네
    return new_graph
    
def bfs(x,y):
    queue=deque()
    queue.append((x,y))
    
    block_cnt, rainbow_cnt = 1, 0 
    blocks, rainbows = [[x,y]], []

    while queue:
        x,y=queue.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            
            if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny] and graph[nx][ny] == graph[x][y]:
                visited[nx][ny] = 1
                queue.append([nx, ny])
                block_cnt += 1
                blocks.append([nx, ny])
            # 범위 안이면서 방문 안한 무지개 블록인 경우
            elif 0 <= nx < N and 0 <= ny < N and not visited[nx][ny] and graph[nx][ny] == 0:
                visited[nx][ny] = 1
                queue.append([nx, ny])
                block_cnt += 1
                rainbow_cnt += 1
                rainbows.append([nx, ny])
    # 무지개 블록은 다시 돌려야하니까,,, 일반블록, 무지개 블록 나눈듯
    for x,y in rainbows:
        visited[x][y] = 0
    return [block_cnt, blocks+rainbows]

def remove(a):
    for x,y in a:
        graph[x][y]=-2
        
# 상하좌우
dx=[-1,1,0,0]
dy=[0,0,-1,1]
N,M=map(int, input().split())
graph=[]
for i in range(N):
    graph.append(list(map(int, input().split())))
    
score=0
while True:
    visited=[[0]*N for _ in range(N)]
    blocks=[]
    # 문제는, 가장 클 블록 개수를 찾았는데 그 좌표들을 다 어떻게 -2로 만들지(좌표값을 어케 저장하지)
    for i in range(N):
        for j in range(N):
            if graph[i][j]>=1 and visited[i][j]==0:
                # 여기서도 방문 해줘야....
                visited[i][j]=1
                # 일반 블록을 반드시 포함해야하므로, 일반 블록 중심으로 bfs 돌리기
                block_info=bfs(i,j)
                print(block_info)
                if block_info[0]>=2:
                    blocks.append(block_info)
    #print(blocks)
    blocks.sort(reverse=True)
    if not blocks:
        break
    remove(blocks[0][1])   
    score += blocks[0][0]**2
    
    earth(graph)
    graph=rotate()
    earth(graph)
print(score)


# -

# 내 bfs
def bfs(x,y):
    location=[]
    count=1
    queue=deque()
    queue.append((x,y))
    location.append((x,y))

    while queue:
        x,y=queue.popleft()
        count +=1
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            
            if nx<0 or ny<0 or nx>N-1 or ny>N-1:
                continue
            # 검은 블록 포함 금지
            if graph[nx][ny]==-1 or visited[nx][ny]==1:
                continue
            # 일반 블록 색은 하나, 무지개 블록이어도 추가
            if graph[nx][ny]==graph[x][y] or graph[nx][ny]==0:
                queue.append((nx,ny))
                visited[nx][ny]=1
                location.append((nx,ny))
    for i in range(N):
        for j in range(N):
            if graph[i][j]==0:
                visited[i][j]=0
    return [count, location]

