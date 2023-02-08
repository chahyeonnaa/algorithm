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
N=int(input())
S=[]
result=0
for _ in range(N):
    S.append(int(input()))
    
S.sort(reverse=True)
for i in range(N):
    S[i]=S[i]-(i)
    if S[i]>0:
        result+=S[i]
print(result)
    
# -


