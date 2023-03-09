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
# 성공!
result=[]
def dfs(x):
    if len(result)==6:
        print(*result)
        return
    for i in range(x, len(S)):
        result.append(S[i])
        dfs(i+1)
        result.pop()
        
while(1):
    S=list(map(int, input().split()))
    if S[0]==0:
        break
    dfs(1)
    result=[]
    print()
# -


