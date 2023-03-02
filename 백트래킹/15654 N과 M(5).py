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
def dfs():
    if len(result)==M:
        print(*result)
        return
    
    for i in range(N):
        if S[i] not in result:
            result.append(S[i])
            dfs()
            result.pop()

N,M=map(int, input().split())
S=list(map(int, input().split()))
S.sort()
result=[]
dfs()
# -


