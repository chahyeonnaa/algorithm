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
N,M=map(int, input().split())
S=[]
for _ in range(2):
    A=list(map(int, input().split()))
    S.append(A)

A=S[0]+S[1]
A.sort()
print(*A)

# +
# 투 포인터 쓰기
N,M=map(int, input().split())
A=list(map(int, input().split()))
B=list(map(int, input().split()))

a=0
b=0
result=[]
while a!=len(A) or b!=len(B):
    if a==len(A):
        result.append(B[b])
        b+=1
    elif b==len(B):
        result.append(A[a])
        a+=1
    else:
        if A[a]<B[b]:
            result.append(A[a])
            a+=1
        else:
            result.append(B[b])
            b+=1
            
print(*result)
