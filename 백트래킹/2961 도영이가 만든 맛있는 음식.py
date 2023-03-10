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

# 얼마가 됐을 때 기록하는게 아니라 모든 경우에서 두 값의 최소값을….. 
# 하나만 고를수도 있고, 다 고를수도 있고 모~~~든 경우의 수를 다 따지는 브루트포스
# 메인에서 dfs를 부를 때, 배열 개수만큼 반목문을 돌린다.... 
def dfs(depth, start):
    global result
    if depth==R:
        sin=1
        son=0
        for i in arr:
            sin *=i[0]
            son +=i[1]
        if result>abs(sin-son):
            result=abs(sin-son)
        return
    # for문에 매개변수 쓰는 이유 : 1234일때 12랑 21이랑 같게 취급하는 경우!
    for i in range(start, N):
        arr.append(S[i])
        dfs(depth+1, i+1)
        arr.pop()
N=int(input())
S=[]
arr=[]
result=1000000000
for i in range(N):
    S.append(list(map(int, input().split())))
for i in range(1, N+1):
    R=i
    dfs(0,0)
print(result)


