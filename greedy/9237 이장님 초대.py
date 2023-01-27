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
M=list(map(int, input().split()))
M.sort(reverse=True)

day=[0]*(N+1)
for i in range(N):
    day[i]=M[i]+(i+1)
    
print(max(day)+1)
# -


