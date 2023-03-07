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
# 배열 pop, append하는 방법 말고도 visited만을 이용해서 리턴 조건을 만드는게 훨씬 편함
# 깊이를 인자로 넘겨서 재귀 호출 횟수를 세는거지,,,
# visited 체커 잘 활용하기!
# 나는 배열을 만들어서 숫자를 골라 넣고, 그 숫자 인덱스에 해당하는 값들을 더해주려고 했음
# 그러면 능력치를 구할 때 너무 복잡해진다.
def dfs(depth, x):
    if depth == N//2:
        A,B=0,0
        for i in range(N):
            for j in range(N):
                if visited[i] and visited[j]:
                    A += S[i][j]
                elif not visited[i] and not visited[j]:
                    B += S[i][j]
        result.append(abs(A-B))        
        return 
    
    for i in range(x,N):
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


