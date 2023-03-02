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

N,M=map(int, input().split())
S=[]
def dfs(x):
    if len(S)==M:
        print(*S)
        return
    for i in range(x, N+1):
        S.append(i)
        dfs(i)
        S.pop()
dfs(1)


