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
from collections import deque
# 핵심 : 방향전환, (오른쪽을 시작으로) R이면 위-> 좌 -> 아래 -> 우(0123)
# L이면 아래 -> 좌 -> 위 -> 우(0321)

# 그래프를 0으로 채우고, 사과는 2, 뱀은 1로 한다
# 머리를 늘리고, 꼬리칸을 비워주고 해야되기 때문에 큐를 쓴다.(선입 선출)
# 몇초후에 C로 방향 전환은 딕셔너리 사용,,
# 매 이동마다 초를 세는데, 그 초가 딕셔너리에 있으면 -> 방향을 바꾼다
# 인덱스 초과하면 종료(벽에 부딪히면)

# 뱀을 큐로 구현한게 신의 한수인듯,,,,,
# 그래프 값은 1로 만들고, 늘어난 몸의 좌표를 큐에 추가, 꼬리를 비우면 pop
# 꼬리칸 비우기 pop하려고 큐가 필요한 것
# 자기 몸을 만났을때가 생각하기 어려웠는데, 뱀의 몸을 그래프 값을 1로 해서 값이 1이면 만난거다.. 왕
# 방향전환 순간들을 딕셔너리로 구현해서, if cnt in snake: 이런식으로 키값과 벨류를 쉽게 확인가능..
N=int(input())
K=int(input())
graph=[[0]*N for _ in range(N)]
dx=[0,1,0,-1]
dy=[1,0,-1,0]
for i in range(K):
    A,B=map(int, input().split())
    graph[A-1][B-1]=2
L=int(input())
snake=dict()
queue=deque()
queue.append((0,0))

x,y=0,0
graph[x][y]=1
cnt=0
direction=0

def turn(alpha):
    global direction
    if alpha=="L":
        direction = (direction-1)%4
    else:
        direction = (direction+1)%4
for i in range(L):
    A,B=input().split()
    snake[int(A)]=B
    
while True:
    cnt +=1
    x += dx[direction]
    y += dy[direction]
    
    if x<0 or y<0 or x>=N or y>=N:
        break
    
    # 사과가 있을때
    if graph[x][y]==2:
        graph[x][y]=1
        queue.append((x,y))
        # 시간되면 방향전환
        if cnt in snake:
            turn(snake[cnt])
    # 사과가 없을때
    elif graph[x][y]==0:
        graph[x][y]=1
        queue.append((x,y))
        tx,ty=queue.popleft()
        graph[tx][ty]=0
        # 시간되면 방향전환
        if cnt in snake:
            turn(snake[cnt])
    # 자기자신의 몸과 부딪히는 경우
    else:
        break
print(cnt)
# -


