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
S=list(map(int, input().split()))
S.sort()
result=[]
def dfs(x):
    if len(result)==M:
        print(*result)
        return
    for i in range(x,N):
        result.append(S[i])
        dfs(i)
        result.pop()
        
dfs(0)
# -


