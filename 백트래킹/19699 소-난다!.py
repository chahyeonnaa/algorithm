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
# 2,3이랑 3,2랑 같게 침 -> 이거 고려안해주면 시간 초과임
# result 배열 안쓰고 체커만 써서 하는 방법이 더 간단함
def is_prime(x):
    for i in range(2,x):
        if x%i==0:
            return False
    return True

def dfs(x):
    if len(result)==M:
        if is_prime(sum(result)):
            A.add(sum(result))
            return
    for i in range(x,N):
        if visited[i]==0:
            result.append(S[i])
            visited[i]=1
            dfs(i+1)
            result.pop()
            visited[i]=0
        
N,M=map(int, input().split())
S=list(map(int, input().split()))
result=[]
A=set()
visited=[0]*N
dfs(0)
if len(A)!=0:
    print(*sorted(list(A)))
else:
    print(-1)
# -


