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

A=list(map(int, input().split()))
B=list(map(int, input().split()))

result=0

for _ in range(N):
    result += min(A)*max(B)
    A.remove(min(A))
    B.remove(max(B))
    
print(result)

       
