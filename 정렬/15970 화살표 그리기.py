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
# 74퍼에서 틀림. 왜지?
N=int(input())
S=[[] for _ in range(N+1)]
for _ in range(N):
    A,B=map(int, input().split())
    S[B].append(A)
    
result=0
for i in range(N):
    S[i].sort()
    R=len(S[i])
    if R>=2:
        result += (S[i][1]-S[i][0])
        result += (S[i][R-1]-S[i][R-2])
        for j in range(1,R-1):
            Q=S[i][j]-S[i][j-1]
            W=S[i][j+1]-S[i][j]
            result += min(Q,W)
print(result)
# -


