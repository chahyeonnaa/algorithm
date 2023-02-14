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
for _ in range(N):
    a,b,c,d=map(str, input().split())
    S.append([a, int(b), int(c), int(d)])
    
S.sort(key=lambda x: (x[3], x[2], x[1]))
print(S)
# -


