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
# 놓치고 있는 부분 : 첫행첫열을 마지막행 마지막열과 이어준다는 것..
# i+(x[A-1]*B%N) 이렇게 해서 한참을 헤맸다. 제발 대충 생각하지말자
# visted 배열 쓰면 안됨. 첫번째 조건문에서 값을 바꿔주면 올바르게 못돌림요 ㅠ
# 초기 구름 값 좌표를 따로 temp에 저장하고, 움직인 구름 좌표 값을 또 따로 저장
# 새 구름 좌표를 따로 만들어서 그걸 다시 temp에 넣어주자
# 어라라.. 시간초과 -> (i,j) not in moved_clouds: 이부분이 오래걸림
# 구름이 있던 자리인지 검사하는 과정! -> visited 배열로 해주자
# 처음으로 설계부터 코드까지 다 혼자 해봄! 희망이 보인다...

N,M=map(int, input().split())
S=[]
# 좌 좌위 위 오위 우 우아래 아래 왼아래
x=[0,-1,-1,-1,0,1,1,1]
y=[-1,-1,0,1,1,1,0,-1]

for i in range(N):
    S.append(list(map(int, input().split())))

temp=[(N-1, 0), (N-1, 1), (N-2, 0), (N-2, 1)]
for _ in range(M):

    moved_clouds=[]
    A,B=map(int, input().split())
    
    # 구름 이동
    for i,j in temp:
        nx=(i+x[A-1]*B)%N
        ny=(j+y[A-1]*B)%N
        moved_clouds.append((nx,ny))
        # 물 뿌리기
        S[nx][ny] +=1
        
    visited=[[0]* N for _ in range(N)]
    for i,j in moved_clouds:
        visited[i][j]=1
        
    # 대각선 방향 물 있는지 검사
    for i,j in moved_clouds:
        result =0
        for k in range(1,8,2):
            nx=i+x[k]
            ny=j+y[k]
                    
            if nx<0 or ny<0 or nx>=N or ny>=N:
                continue
            if S[nx][ny]>=1:
                result+=1
        S[i][j] += result
    new_clouds=[]
    # 구름 만들기
    for i in range(N):
        for j in range(N):
            if S[i][j]>=2 and visited[i][j]==0:
                S[i][j] -=2
                new_clouds.append((i,j))
    temp=new_clouds

real=0
for i in range(N):
    for j in range(N):
        real += S[i][j]
print(real)
            
    
    
            
            
# -

# ##### 
