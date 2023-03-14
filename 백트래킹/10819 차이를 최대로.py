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
# 모든 경우 다 해봐야함!
# 똑같은거 못 뽑음 -> visited 체커 활용
def dfs():
    global R
    if len(result)==N:
        sum_m=0
        for i in range(N-1):
            sum_m += abs(result[i]-result[i-1])
        R=max(sum_m,R)
        return
    
    for i in range(N):
        if visited[i]==0:
            result.append(S[i])
            visited[i]=1
            dfs()
            visited[i]=0
            result.pop()
        
N=int(input())
S=list(map(int, input().split()))
result=[]
R=0
visited=[0]*N
dfs()
print(R)

# -


