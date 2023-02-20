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
# 놓치는 케이스 없게 꼼꼼히 생각하자
# 간단히 생각하면, 각 리스트 값과 B의 차이, 플마로 조정가능한 값의 min을 뽑으면 된다..
A,B=map(int, input().split())
N=int(input())
S=[]
result=abs(B-A)
num=0

for _ in range(N):
    S.append(int(input()))

S.sort()


if S[0]>B:
    num=abs(B-S[0])
else:
    for i in range(N):
        if S[i]>B:
            D=S[i]-B
            F=B-S[i-1]
            num=min(D,F)
            break
        if i== N-1:
            num=B-S[i]
if B in S:
    print(1)
else:
    print(min(result, num+1))
# -


