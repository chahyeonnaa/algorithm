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
# 첫 시도 : 재귀함수,, 쓰면 앙돼 
import sys
sys.setrecursionlimit(10**6)
def dfs(x):
    global money, result
    if x+T[x]==N:
        money += M[x]
        result=max(money,result)
        return
    money += M[x]
    dfs(x+T[x])
    
N=int(input())
T=[0]*(N+1)
M=[0]*(N+1)
money=0
result=0
for i in range(1, N+1):
    A,B=map(int, input().split())
    T[i]=A
    M[i]=B

for i in range(1,N+1):
    if i+T[i]>N:
        T[i]=0
        
for i in range(1, N+1):
    money=0
    if T[i]==0:
        break
    dfs(i)
print(result)

# +
N=int(input())
T=[0]*(N+1)
M=[0]*(N+1)
money=0
result=0
for i in range(1, N+1):
    A,B=map(int, input().split())
    T[i]=A
    M[i]=B

for i in range(1, N+1):
    money=0
    time=0
    while True:
        if time>N:
            break
        time=i+T[i]
        money += M[i]
        if time==N+1 and T[i]==1:
            money += M[i]
            break
        i=time
    result=max(money, result)
print(result)
# -

# ###### 
