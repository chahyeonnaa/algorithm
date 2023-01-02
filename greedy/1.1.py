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
# 그리디_ 2839 설탕 배달
# dp로 풀어본 문제

N=int(input())

result=0

while N >=0:
    if N % 5==0:
        result+= (N//5)s
        print(result)
        break
    N=N-3
    result+=1
else: # while 문이 거짓일 시
    print(-1)
