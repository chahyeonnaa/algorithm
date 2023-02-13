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
S=[]
for i in range(9):
    S.append(int(input()))
    
sum_S=sum(S)
A=0
B=0
for i in range(8):
    for j in range(i+1, 9):
        if sum_S-(S[i]+S[j])== 100:
            A=S[i]
            B=S[j]
            break
S.remove(A)
S.remove(B)
S.sort()
print(*S, sep="\n")
# -


