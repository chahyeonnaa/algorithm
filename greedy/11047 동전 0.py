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
# 11047 동전 0

# 가진 동전 종류 N, 합을 K로 만들기, 필요한 동전 개수의 최솟값
# 동전 내림차순 정렬해서, K보다 크면 패스, K보다 작으면 계산

N,K=map(int, input().split())
money=[]
result=0
for i in range(N):
    money.append(int(input()))
    
money.sort(reverse=True)

for i in money:
    if K==0:
        break
    if i>K:
        continue
    result +=(K//i)
    K=(K%i)
print(result)

# -


