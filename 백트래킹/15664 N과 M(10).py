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

def dfs(x):
    if len(result)==M:
        print(*result)
        return
    A=0
    for i in range(x,N):
        if A!=S[i]:
            result.append(S[i])
            A=S[i]
            dfs(i+1)
            result.pop()
N,M=map(int, input().split())
S=list(map(int, input().split()))
S.sort()
result=[]
dfs(0)


