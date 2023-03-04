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

# 시간초과 -> N이 10,000까지라 백트래킹으로 풀이가 불가능한 문제였음
import sys
sys.setrecursionlimit(10**6)
N=int(input())
S=list(map(int, input().split()))
result=[]
A=[]
def dfs():
    if len(result)==len(S):
        A.append(list(result))
        return
    for i in range(1,N+1):
        if i not in result:
            result.append(i)
            dfs()
            result.pop()
dfs()
t=A.index(S)
if t==len(A)-1:
    print(-1)
else:
    print(*(A[t+1]))

# +
# https://rrojin.tistory.com/46 / 어떻게 이런 생각을...
