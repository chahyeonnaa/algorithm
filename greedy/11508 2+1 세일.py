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
# 2,5,8,..번째마다 빼주려고 했는데,, 로직이 복잡함
# 다 더해서 2,5,8번째마다 빼주면 간단....
# 생각을 넗히자
N=int(input())
S=[]
for _ in range(N):
    S.append(int(input()))
    
S.sort(reverse=True)
result=sum(S)

for i in range(2,N,3):
    result -= S[i]
    
print(result)
