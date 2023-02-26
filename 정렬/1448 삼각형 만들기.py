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
# 가장 긴 변의 길이는 다른 두 변의 길이 합보다 작아야함
# 세 변의 길이 합의 최댓값
# 시간초과...
N=int(input())
S=[]
for _ in range(N):
    S.append(int(input()))
S.sort(reverse=True)
result=0
for i in range(N-2):
    if S[i]<S[i+1]+S[i+2]:
        result += (S[i]+S[i+1]+S[i+2])
        break

if result==0:
    print(-1)
else:
    print(result)
# -


