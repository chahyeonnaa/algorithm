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
S={}
result=0
A=[]
for i in range(8):
    S[i]=int(input())
    
S=sorted(S.items(), key= lambda x: (-x[1]))
for i in range(5):
    result+=S[i][1]
    A.append(S[i][0]+1)
A.sort()
print(result)
print(*A)
# -


