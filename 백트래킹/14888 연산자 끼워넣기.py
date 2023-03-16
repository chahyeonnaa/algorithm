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

# 재귀 끝나면 매개변수 값은 원래 값으로 컴백
# total 값을 0으로 하면 곱하기에서 문제 생김
def dfs(depth, plus, minus, mul, divide, total):
    global num_min,num_max
    if depth==N:
        num_max=max(num_max, total)
        num_min=min(num_min, total)
        return
    if plus:
        dfs(depth+1,plus-1, minus, mul, divide, total+A[depth])
    if minus:
        dfs(depth+1,plus, minus-1, mul, divide, total-A[depth])
    if mul:
        dfs(depth+1,plus, minus, mul-1, divide, total*A[depth])
    if divide:
        dfs(depth+1,plus, minus, mul, divide-1, int(total/A[depth]))
N=int(input())
A=list(map(int, input().split()))
plus, minus, mul, divide=map(int, input().split())
total=A[0]
num_min=1e9
num_max=-1e9
dfs(1,plus, minus, mul, divide, total)
print(num_max)
print(num_min)


