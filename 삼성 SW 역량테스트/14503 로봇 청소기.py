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
# 전형적인 시뮬레이션 문제! 
# 알고리즘 없이 문제에서 요구하는 내용을 오류없이 성실하게 구현만 할 수 있다면 풀 수 있음

# 포인트 1. 반시계 방향으로 90도 회전
# 0,1,2,3(북 동 남 서) -> 3 0 1 2
# 식으로 표현하면 d=(d+3)%4
# 이걸 쓰면, 북동남서 배열 S=[0,1,2,3]이 필요 없고 조건문 안쓰고 편하게 반복문 돌리면 된다.
# 나는 북일 때 서, 동일때 북,, 이런식으로 조건문 써서 할려고 했음.

# 포인트 2. 바라보는 방향을 유지한 채로 전진, 후진
# dr=[-1,0,1,0], (북동남서)
# dc=[0,1,0,-1]
# 현 위치 : r,c / 바라보는 방향 : d
# 전진 : nr=r+dr[d] / 후진 : nr=r-dr[d]

# 전제 프로세스 : 무한 반복문 + 탈출 조건 : 후진했을 때 벽인 경우
# 현 위치 기준 4방향을 확인해야함.(청소할 수 있는 영역이 있는지)
# -> 여기서 확인할 때 일반적으로 반복문 i를 쓰는게 아니라 d=(d+3)%4 이 식을 i로 쓴다...!!
# ** 중요 ** 왜냐면 청소할 수 있는 영역이 있으면, 반시계 회전 후에 한칸 전진하고, 그곳을 청소함
# 여기서 한 칸 전진이, 주변 4방향이랑 같은 말임

# 청소를 할 수 있는 경우
# 현위치 nr, nc가 인덱스 확인, 벽인지 확인, 방문했던 곳인지 확인해서 조건 통과되면 청소하고 현위치 갱신까지 해줘야함
# flag 값도 1으로 해줘야 아래 조건문 통과 안함

# (flag가 그대로 0일 경우)
# 청소할 영역이 없는 경우(반복문을 모두 돌았을 때)
# 후진하는데, 후진했을 때 벽이면 프로세스 종료
# 벽 아니면, 현 위치 갱신



# +
N,M=map(int, input().split())
r,c,d=map(int, input().split())
graph=[]
visited=[[0]*M for _ in range(N)]
# 북 동 남 서
dr=[-1,0,1,0]
dc=[0,1,0,-1]
cnt=1

# 처음 위치 방문 표시 해야한다
visited[r][c]=1

for i in range(N):
    graph.append(list(map(int, input().split())))
    
while True:
    flag=0
    
    for _ in range(4):
        d=(d+3)%4
        nr=r+dr[d]
        nc=c+dc[d]
        
        if visited[nr][nc]==0:
            if graph[nr][nc]==0 and nr>=0 and nr<N and nc>=0 and nc<M:
                visited[nr][nc]=1
                cnt +=1
                flag=1
                r=nr
                c=nc
                break
    if flag==0:
        if graph[r-dr[d]][c-dc[d]]==1:
            break
        else:
            r=r-dr[d]
            c=c-dc[d]
        
print(cnt)
    
# -

# # 
