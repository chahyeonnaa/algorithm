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
# 하나의 리스트로 들어가서 타입오류..난..다
# 딕셔너리로 풀기 실패
N,K=map(int, input().split())
J={}
for i in range(N):
    M=[]
    A,G,S,R=map(int, input().split())
    M.append(G)
    M.append(S)
    M.append(R)
    J[A]=M
    
    
print(J)
J=sorted(J.items(), key= lambda x: (-x[1], -x[2], -x[3]))
print(J)

# +
# 쉽지 않네.....
N,K=map(int, input().split())
S=[]
for _ in range(N):
    S.append(list(map(int, input().split())))
    
S.sort(key=lambda x: (-x[1], -x[2], -x[3]))

for i in range(N):
    if S[i][0]==K:
        index=i
        
for i in range(N):
    if S[index][1:]==S[i][1:]:
        print(i+1)
        break
# -


