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
count=[]
H=[]
for i in range(N):
    A=input()
    if A in S:
        b=S.index(A)
        count[b]+=1
    else:
        S.append(A)
        count.append(1)

m=max(count)
for i,v in enumerate(count):
    if v==m:
        H.append(S[int(i)])
H.sort()
print(H[0])

# +
# 딕셔너리로 풀기 - 내가 훨씬 빠르지롱....
n=int(input())
dic={}
for i in range(n):
    a=input()
    if a not in dic:
        dic[a]=1
    else:
        dic[a]+=1
        
num=max(dic.values())
a=[]
# 딕셔너리 이렇게 표현도 가능
# dic[i] -> values
# i -> key
for i in dic:
    if num==dic[i]:
        a.append(i)
        
a.sort()
print(a[0])
# -


