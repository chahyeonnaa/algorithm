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
N,M=map(int, input().split())
S=[]
for _ in range(N):
    S.append(input())
    
result=''
count=0
for i in range(M):
    a,c,g,t=0,0,0,0
    for j in range(N):
        if S[j][i]=="A":
            a+=1
        elif S[j][i]=="C":
            c+=1
        elif S[j][i]=="G":
            g+=1
        elif S[j][i]=="T":
            t+=1
            
    if max(a,c,g,t)==a:
        result+='A'
        count += c+g+t
    elif max(a,c,g,t)==c:
        result+='C'
        count += a+g+t
    elif max(a,c,g,t)==g:
        result+='G'
        count += a+c+t
    elif max(a,c,g,t)==t:
        result+='T'
        count += a+g+c

print(result)
print(count)
