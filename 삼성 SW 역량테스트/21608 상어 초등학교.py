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
# 역대급으로 어려웠음, 정답 코드를 봐도 도저히 이해가 안됐다...하ㅏ
# 전체 프로세스 : 사람을 배치할 때 교실 전체를 돌면서 자리별로 확인
# 1. 주변에 좋아하는 사람 몇명?/ 2. 주변에 비어 있는 자리 몇개?
# 처음 학생 자리는 무조건 [1,1]! 이건 내가 알아냄
# sum_like, sum_empty를 자리별로 구해서 람다식써서 정렬하는게 핵심
N=int(input())
p=N*N
# 교실 자리 배치도
classroom=[[0]*N for _ in range(N)]
# 각 학생들이 좋아하는 사람 리스트
like_room=[[] for _ in range(p+1)]

dy=[-1,1,0,0]
dx=[0,0,-1,1]
for i in range(p):
    array= list(map(int, input().split()))
    
    like=array[1:]
    like_room[array[0]]=like
    
    if i==0:
        classroom[1][1]=array[0]
        continue
    temp=[]   
    for a in range(N):
        for b in range(N):
            sum_like, sum_empty=0,0
            if classroom[a][b]!=0:
                continue
            for k in range(4):
                nx=a+dx[k]
                ny=b+dy[k]
                    
                if nx<0 or ny<0 or nx>=N or ny>=N:
                    continue
                if classroom[nx][ny] in like:
                    sum_like +=1
                if classroom[nx][ny]==0:
                    sum_empty +=1
            temp.append((sum_like, sum_empty,(a,b)))
    temp.sort(key=lambda x:(-x[0],-x[1],x[2]))
    classroom[temp[0][2][0]][temp[0][2][1]]=array[0]
                            
result=0
for i in range(N):
    for j in range(N):
        answer=0
        for k in range(4):
            nx=i+dx[k]
            ny=j+dy[k]
                    
            if nx<0 or ny<0 or nx>=N or ny>=N:
                continue
            if classroom[nx][ny] in like_room[classroom[i][j]]:
                answer +=1
                continue
        if answer !=0:
            result += (10 **(answer-1))                    
print(result)       
    
# -


