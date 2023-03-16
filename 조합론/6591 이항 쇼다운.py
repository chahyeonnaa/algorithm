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

# nCk 구하기
import math
while True:
    N,k=map(int, input().split())
    if N==0 and k==0:
        break
    print(math.comb(N,k))


# nCk = n!/(n-k)!k!
def fac(n):
    num=1
    for i in range(2,n+1):
        num *=i
    return num
while(1):
    N,k=map(int, input().split())
    if N==0 and k==0:
        break
    print(fac(N)//fac(N-k)*fac(k))


