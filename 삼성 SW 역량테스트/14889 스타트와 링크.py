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
# 어쨌거나 두명을 고르는건데, 12나 21이나 똑같기 때문에 매개변수로 x넘겨줌
# 함수 안에서 visited 체커로 짝 지어서 계산하기
# ~와 ~의 차이의 최솟값을 구한다? -> 모든 경우를 다 따져봐야함 -> 백트래킹
def dfs(depth, x):
    if depth == N//2:
        A,B=0,0
        for i in range(N):
            for j in range(N):
                if visited[i]==0 and visited[j]==0:
                    A += S[i][j]
                elif visited[i]==1 and visited[j]==1:
                    B += S[i][j]
        result.append(abs(A-B))
        return
    for i in range(x, N):
        if visited[i]==0:
            visited[i]=1
            dfs(depth+1, i+1)
            visited[i]=0

N=int(input())
S=[]
result=[]
visited=[0]*(N)
for i in range(N):
    S.append(list(map(int, input().split())))  
dfs(0,0)
print(min(result))
# -


