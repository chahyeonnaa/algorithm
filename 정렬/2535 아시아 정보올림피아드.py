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
count=0

for i in range(N):
    S.append(list(map(int, input().split())))
    
S.sort(key=lambda x: -x[2])
print(S[0][0], S[0][1])
print(S[1][0], S[1][1])

# 금은동 셋다 못가져간다. 두개만 가능.
# 1,2등이 같으면 3등은 밀려남
if S[0][1] == S[1][0]:
    count=1
    
for i in range(2, N):
    if count==0:
        print(S[i][0], S[i][1])
        break
    else:
        if S[1][0] != S[i][0]:
            print(S[i][0], S[i][1])
            break
# -


