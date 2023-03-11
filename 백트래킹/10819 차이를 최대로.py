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

N=int(input())
S=list(map(int, input().split()))
result=[]
visited=[0]*N
number=0
def dfs():
    global number
    if len(result)==N:
        total=0
        for i in range(N-1):
            total += abs(S[i]-S[i-1])
        number = max(number, total)
        return
        
    for i in range(N):
        if visited[i]==0:
            result.append(S[i])
            visited[i]=1
            dfs()
            result.pop()
            visited[i]=0
print(number)
