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
# 다솜이가 제일 큰수가 될 때 까지, 제일 큰수에서 1씩 가져온다. 
# 성공!
N=int(input())
S=[]
for _ in range(N):
    S.append(int(input()))
result=S[0]   

while True:
    if len(S)==1:
        break
    M=max(S)
    A=[]
    for i,v in enumerate(S):
        if v==M:
            A.append(i)
    if len(A)>1 and M==S[0]:
        S[0]+=1
        break
    elif M==S[0]:
        break
        
    x=S.index(M)
    S[x]-=1
    S[0]+=1

        
print(S[0]-result)
    
    
# -




