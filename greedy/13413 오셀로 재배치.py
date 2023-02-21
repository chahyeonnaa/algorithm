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
# 인접한 두개만 바꿀 수 있는것 아님..!
T=int(input())
arr=[]
for _ in range(T):
    N=int(input())
    start=list(input())
    result=list(input())
    cnt=0
    change=0
    
    for i in range(N-1):
        if start[i]=='B' and start[i+1]=='W'and result[i]=="W" and result[i+1]=="B":
            start[i]="W"
            start[i+1]="B"
            change +=1
        elif start[i]=='W' and start[i+1]=='B'and result[i]=="B" and result[i+1]=="W":
            start[i]="B"
            start[i+1]="W"
            change +=1
    
    for j in range(N):
        if start[j]!=result[j]:
            start[j]=result[j]
            cnt+=1
    arr.append(cnt+change)
    
for i in arr:
    print(i)
# -

2 3 3 
