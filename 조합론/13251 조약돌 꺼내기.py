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

# 콤비네이션 라이브러리 사용
import math
M=int(input())
S=list(map(int, input().split()))
K=int(input())
result=math.comb(sum(S),K)
num=0
for i in range(len(S)):
    num += math.comb(S[i],K)
print(num/result)


