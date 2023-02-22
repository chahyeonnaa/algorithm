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
# 달걀 개수 예외처리 주의!
N,M=map(int, input().split())
S=[]
for _ in range(M):
    S.append(int(input()))
    
S.sort(reverse=True)
result=[]
a=1
for i in range(M):
    result.append(S[i]*a)
    a+=1
    if a>N:
        break

R=max(result)
f=result.index(R)
w=R//(f+1)
print(w, R)

# -


