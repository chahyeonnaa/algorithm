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
K=int(input())

for i in range(K):
    score=list(map(int, input().split()))
    del score[0]
    score.sort()
    
    C=[]
    print("Class", i+1)
    A=max(score)
    B=min(score)
    C=[]
    for j in range(len(score)-1):
        C.append(score[j+1]-score[j])
    print("Max "+str(A)+","+" Min "+str(B)+","+" Largest gap "+str(max(C)))
    
# -


