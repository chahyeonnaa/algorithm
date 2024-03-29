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
# 백트래킹 문제, 벽을 세울 수 있는 경우마다 다 체크해서 확인하는 문제
# 벽을 세울 수 있는 조합 다 구해서, 각각 값을 bfs로 확인!
# 나는 2 주변 상하좌우를 검사해서, 연결요소가 끊길 수 있는 부분에 벽을 세우는 것으로 접근 했음.
# -> 구현하기 어렵다. 연결요소 끊기는 부분을 어떻게 찾지?

# 벽 3개를 세우고, 바이러스 퍼뜨리기 -> 벽세우기 함수(재귀로 구현=조합) 안에서 bfs 호출
# 벽 세우기 함수 : 3개의 벽을 세울 수 있는 경우의 수를 다 찾자(조합!!!)(재귀!!!)

# 경우의 수를 각각 찾을 때 마다, bfs 호출해서 퍼뜨리고 결과 확인
# 바이러스가 있는 좌표값을 큐에 넣자
# bfs를 호출한 순간의 그래프 값을 깊은 복사해야함. 그래야 검사하지.
# 값이 2인 주변(상하좌우) 다 확인해서 0이면 2로 바꿔주기(퍼뜨리기)
# 2인 곳 = 바이러스가 있는 좌표 값을 큐에 넣어주는게 신의 한수. 아 어렵다 ㅜ 
# -> 2로 바꿨으면 그 좌표 값을 또 큐에 넣어줘야함. 그래야 점점 퍼질 수 이씀(*중요*)

# 다 퍼뜨렸으면, 감염되지 않은 영역 계산 -> 글로벌 변수 result에 저장해놓기
# bfs 끝났으면, 다음 벽(조합) 구해서 다시 bfs() 함수 돌리기
# 와... 이런 구조라니. 

# 이렇게 안하고, 처음부터 벽을 세울 수 있는 조합을 한꺼번에 구해서...?
# 그러면 또 어딘가에 넣어놔야 되니까 힘들겠지. 한두개도 아닐건데...
# 그래서 하나 구하고, 계산하고, 하나 구하고, 하나 계산하고 이걸 반복
# 이게 바로 재귀함수 다 !
from collections import deque
import copy

def wall(count):
    if count==3:
        bfs()
        return
    
    for i in range(N):
        for j in range(M):
            if graph[i][j]==0:
                graph[i][j]=1
                wall(count+1)
                graph[i][j]=0

def bfs():
    queue=deque()
    test=copy.deepcopy(graph)
    
    for i in range(N):
        for j in range(M):
            if test[i][j]==2:
                queue.append((i,j))
    while queue:
        x,y=queue.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            
            if (0<=nx<N) and (0<=ny<M):
                if test[nx][ny]==0:
                    test[nx][ny]=2
                    queue.append((nx,ny))
    global result
    count=0
    for i in range(N):
        for j in range(M):
            if test[i][j]==0:
                count+=1
    result=max(result, count)
        
# 상,하,좌,우       
dx=[-1,1,0,0]
dy=[0,0,-1,1]
result=0
N,M=map(int, input().split())
graph=[list(map(int,input().split())) for _ in range(N)]
    
wall(0)
print(result)
    
# -


