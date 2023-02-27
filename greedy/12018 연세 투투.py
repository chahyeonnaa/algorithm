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

# 62퍼에서 틀림 -> 마일리지가 남는 경우를 고려하지 않았음!(혼자 해결 완완~)
n,m=map(int, input().split())
result=[]
for i in range(n):
    A,B=map(int, input().split())
    S=list(map(int, input().split()))
    
    if A<B:
        result.append(1)
    else:
        S.sort(reverse=True)
        result.append(S[B-1])
result.sort()
for i in range(n):
    m -= result[i]
    if m<0:
        print(i)
        break
    elif m==0:
        print(i+1)
        break
if m>0:
    print(n)


