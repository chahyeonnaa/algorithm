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
# 톱니바퀴

# N극 : 0 / S극 : 1
# 1 : 시계방향 / -1 : 반시계방향

# 이슈 1. 극 비교
# 1번 톱니 : 무조건 [2]랑 2번의 6이랑 비교
# 2,3번 톱니 : 양쪽 다 비교
# 4번 톱니 : 무조건 [6]이랑 3번의 [2]랑 비교

# 이슈 2. 회전 방법
# 시계 방향 : i+1번째에 i값 저장(3번째에 2번째 값이 온다)
# 첫번째에 마지막 값이 들어감, 마지막 자리에는 그 이전 값
# 반시계 방향 : i번째에 i+1번째 값이 저장
# 0번째에 1번째가 저장, 마지막 자리에 첫번째 값이 저장
# 이렇게 함수를 만들었는데, deque의 rotate를 쓰면 편하다고함(찾아보기)

# 전체 프로세스 : 재귀함수(계속 돌려야하니까. 재귀함수 쓰는 이유 찾아보기)
# visited 체커 사용. 
# 왼쪽값 [6], 오른쪽값[2]로 지정

# 1번 톱니가 아닌 나머지 다른 톱니들은 [6]과 [2]비교 가능
# [6][2] 이렇게 비교하면(현재 [6]을 가짐) -> 앞에 톱니를 반대로 돌림(값이 다를때)
# 4번 톱니가 아닌 나머지 다른 톱니들은 [2]랑 [6]끼리 비교 가능
# [2][6] 이렇게 비교하면(현재 [2]를 가짐) -> 뒤에 톱니를 돌린다. 

# -> 이렇게 하면 각각 조건에 맞게 다 검사할 수 있음
# 2,3번 톱니는 양쪽 검사 가능..!


# 소감 : 이슈를 찾아서 각각 구현은 하는데, 이 이슈들을 전체적으로 어떻게 적용시킬지 감이 안온다...
# ㅠㅠ 갈길이 멀다. 



# +
# visited 체커도 꼭 써야함
# 아니면 돌렸던 톱니를 또 돌린다...
def clock(graph):
    temp=graph[7]
    for i in range(6,-1,-1):
        graph[i+1]=graph[i]
    graph[0]=temp
def clock_ban(graph):
    temp=graph[0]
    for i in range(7):
        graph[i]=graph[i+1]
    graph[7]=temp

def dfs(x,y):
    global visited
    if visited[x]==0:
        visited[x]=1
        left=graph[x][6]
        right=graph[x][2]
        if y==1:
            clock(graph[x])
        else:
            clock_ban(graph[x])
            
        if x-1>=0 and left!=graph[x-1][2]:
            dfs(x-1,-y)
        if x+1<=3 and right!=graph[x+1][6]:
            dfs(x+1,-y)
graph=[]
for i in range(4):
    graph.append(list(input().rstrip()))
K=int(input())
for i in range(K):
    A,B=map(int, input().split())
    visited=[0]*4
    dfs(A-1,B)

cnt=0
for i in range(4):
    if graph[i][0]=="1":
        cnt += (2**i)
print(cnt)
# -


