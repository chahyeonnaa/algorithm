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
# 왜 틀리지?
# 삐빅 시간초과.. -> 아 input시간 차이 은근 크다!
import sys
input=sys.stdin.readline
N=int(input())
S={}
for _ in range(N):
    a=int(input())
    if a not in S:
        S[a]=1
    else:
        S[a]+=1

# 여기서 리스트로 다시 저장하면 시간초과임
# for i in S:
#     if max(S.values())==S[i]:
#         M.append(int(i))
        
# M.sort()
# print(M[0])

# items를 써서 2차원 배열 형태로 만든 것....?
S=sorted(S.items(), key=lambda x:(-x[1], x[0]))
print(S[0][0])
# -


