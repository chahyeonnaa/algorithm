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

# 조합 공식 : n!/(n-m)!m!
# 1. math 라이브러리 팩토리얼 사용하기
import math
n,m=map(int, input().split())
top=math.factorial(n)
bottom=math.factorial(m)*math.factorial(n-m)
print(top//bottom)


# 2. 재귀함수
def fac(n):
    num=1
    for i in range(2, n+1):
        num *=i
    return num
n,m=map(int, input().split())
print(fac(n)//fac(m)*fac(n-m))

# 3. math 라이브러리 comb 사용
from math import comb
n,m=map(int, input().split())
print(comb(n,m))


