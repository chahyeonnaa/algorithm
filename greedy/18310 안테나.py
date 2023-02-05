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
# 시간초과
import math
N=int(input())
S=list(map(int, input().split()))
A=[]
C=[]
for i in range(len(S)):
    result=0
    for j in range(len(S)):
        result += abs(S[j]-S[i])
    A.append(result)
    
for i in range(len(A)):
    B=min(A)
    if B==A[i]:
        C.append(S[i])
C.sort()
print(C[0])
# -

# 중앙값 개념 생각하면 쉬운 문제 였.다
N=int(input())
S=list(map(int, input().split()))
S.sort()
if N%2==0:
    A=(N // 2)-1
else:
    A=(N // 2)
print(S[A])


