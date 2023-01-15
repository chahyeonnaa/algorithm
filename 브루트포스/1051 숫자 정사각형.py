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
N,M=map(int, input().split())
square=[]
A=min(N,M)
result=0

for i in range(N):
    S=list(input())
    square.append(S)

for i in range(N):
    for j in range(M):
        for k in range(A):
            if i+k<N and j+k<M:
                q1=square[i][j]
                q2=square[i+k][j]
                q3=square[i][j+k]
                q4=square[i+k][j+k]
                
                if q1==q2==q3==q4:
                    result=max(result,(k+1)**2)
                
print(result)