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
# 12퍼에서 틀림
# 이렇게하면 수열이 다 0으로 이루어지고, S가 0일 때 계속 조건문에 걸림
# 어떨때 스택을 쓰면 좋은지 아닌지 구분할 필요가 있다....
def dfs(x):
    global count,result
    if count==S:
        result+=1
        count=0
        return
    
    for i in range(x,N):
        count += A[i]
        dfs(i+1)
        

N,S=map(int, input().split())
A=list(map(int, input().split()))
count=0
result=0
dfs(0)
print(result)


# +
def dfs(x):
    global count
    if sum(result)==S and len(result)>0:
        count+=1
    
    for i in range(x,N):
        result.append(A[i])
        dfs(i+1)
        result.pop()

N,S=map(int, input().split())
A=list(map(int, input().split()))
count=0
result=[]
dfs(0)
print(count)
# -


