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
# 여기서 중요한 포인뜨 : 리스트로 숫자를 쪼갰기 때문에 join으로 숫자 변환
# 숫자 리스트를 숫자로 비교하려면, join으로 문자열 변환 후 다시 숫자로,,
N=list(map(int, input()))
result=[]
S=[]
visited=[0]*len(N)
def dfs():
    if len(result)==len(N):
        a=''.join(map(str,result))
        b=''.join(map(str,N))
        if int(a)>int(b):
            S.append(int(a))
        return
    
    for i in range(len(N)):
        if visited[i]==0:
            result.append(N[i])
            visited[i]=1
            dfs()
            result.pop()
            visited[i]=0
        
dfs()
S.sort()
if len(S)==0:
    print(0)
else:
    print(S[0])
# -


