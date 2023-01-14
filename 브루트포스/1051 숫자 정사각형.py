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
# N이 세로
# 반복문을 중간에 나오려고 하면 힘들다. 걍 다 돌게 해야함
# i,j 반복문 안에서 k를 도는것과 k안에서 i,j 돌리기 이해하기
N,M=map(int, input().split())
square=[]
A=min(N,M)
result=0
for i in range(N):
    S=list(input())
    square.append(S)

for k in range(A-1,-1,-1):
    for i in range(M):
        if result==1:
            break
        for j in range(N):
            
            if i+k>A or j+k>=A:
                continue
                
            q1=square[i][j]
            q2=square[i+k][j]
            q3=square[i][j+k]
            q4=square[i+k][j+k]
        
            if q1==q2==q3==q4:
                print((k+1))
                result=1
                break
# -


