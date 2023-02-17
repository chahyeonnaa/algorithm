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
# 성공!
N,L=map(int, input().split())
S=list(map(int, input().split()))
S.sort()

for i in range(N):
    if S[i]<=L:
        L +=1
    if S[i]>L:
        break
print(L)
# -


