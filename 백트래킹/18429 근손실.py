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
# 증량이 같을 수 있으나, 서로 다른 키트로 간주함
# 중복 선택 안됨
# 자꾸 21퍼에서 틀린다. 왜지..
# 재귀함수에서 넘겨주는 값을 함수 안에서 바꾸면 틀린다.
def dfs(muscle):
    global count
    if len(result)==N:
        count +=1
        return
    for i in range(N):
        if visited[i] or muscle+S[i]-K<500:
            continue
        result.append(S[i]) 
        visited[i]=1
        dfs(muscle+S[i]-K)
        result.pop()
        visited[i]=0
            
N,K=map(int, input().split())
S=list(map(int, input().split()))
visited=[0]*N
result=[]
count=0
#muscle=500
dfs(500)
print(count)


# +
def dfs(t):
    global count
    if len(result)==N:
        count +=1
        return
    for i in range(N):
        if visited[i] or t+S[i]-K<500:
            continue
        result.append(S[i]) 
        visited[i]=1
        dfs(t+S[i]-K)
        result.pop()
        visited[i]=0
            
N,K=map(int, input().split())
S=list(map(int, input().split()))
visited=[0]*N
result=[]
count=0
dfs(500)
print(count)
# -


