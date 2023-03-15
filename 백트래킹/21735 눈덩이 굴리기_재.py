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
# depth : 위치
def dfs(depth, time, size):
    global result
    if depth>=N or time==M:
        result= max(result, size)
        return;

    dfs(depth+1, time+1, size+S[depth+1])
    dfs(depth+2, time+1, (size//2)+S[depth+2])
            
        
N,M=map(int, input().split())
S=[0]+list(map(int, input().split()))
result=0
dfs(0,0,1)
print(result)
# -

r
