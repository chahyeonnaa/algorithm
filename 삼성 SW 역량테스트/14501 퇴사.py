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
# 이렇게 하면 안되는 케이스 너무 많다. 
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

# +
# DP 쓰는 문제
# 뒤에서부터 그 날 상담을 했을 때, 앞으로의 최댓값을 dp에 저장하는거임
# 4일째 상담을 했으면, 5일날 상담 가능
# 3일째 상담을 했으면, 4일 5일 가능
# 2일째 상담을 하면 2일만 가능 -> 20, 2일은 3일보다 값이 작으니까 dp값을 안바꿈
# DP : 큰 문제를 작은 문제로 나누고, 작은 문제를 반복해서 문제를 해결해나감
# 작은 문제는 딱 한번만 풀어야하고, 그 결과는 어딘가(dp)에 기록해야함
N=int(input())
T=[]
M=[]
dp=[]
for i in range(N):
    A,B=map(int, input().split())
    T.append(A)
    M.append(B)
    dp.append(B)
dp.append(0)

for i in range(N-1, -1, -1):
    if T[i]+i>N:
        dp[i]=dp[i+1]
    else:
        dp[i]=max(dp[i+1], M[i]+dp[i+T[i]])
print(dp[0])
# -

# ###### 
