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
# 첫번째 시도: 10%에서 틀렸다.
# 예외가 있음
N,M=map(int, input().split())
J=int(input())
S=[]
location=M
result=0
for i in range(J):
    S.append(int(input()))

for i in range(J):
    if S[i]<(location-M+1):
        continue
    if S[i]<location:
        location= (location-M+1)
        result += (location-S[i])
        location=S[i]+(M-1)
    elif location<S[i]:
        result += (S[i]-location)
        location=S[i]
        
print(result)
    
# -


