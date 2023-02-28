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
n=int(input())
dict={}
for i in range(n):
    file=input().split('.')[1]
    if file not in dict:
        dict[file]=1
    else:
        dict[file] +=1
        
S=list(dict.keys())
S.sort()
for i in S:
    print(i, dict[i])

